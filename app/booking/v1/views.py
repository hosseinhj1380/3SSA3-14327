
from app.booking import selectors,services
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.utils.dateparse import parse_datetime
from .serializer import ReservationRequestSerializer,ReservationResponseSeralizer
from app.booking.helper import best_fit_table
from drf_spectacular.utils import extend_schema
from app.booking.models import Reservation,Table

class ReservationsView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(request=ReservationRequestSerializer, responses=ReservationResponseSeralizer,)
    def post(self, request):
        serializer = ReservationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        start = serializer.validated_data["start_time"]
        end = serializer.validated_data["end_time"]
        individuals_number = serializer.validated_data["individuals_number"]
        tables= selectors.get_available_table(start,end)
        
        fit_table , cost = best_fit_table(tables,individuals_number)

        if fit_table is None:
            return Response({"error":"not possible to reserve"},status.HTTP_406_NOT_ACCEPTABLE)
        
        reserved_table=services.reserve_table(user=request.user,table=fit_table,reserved_seats=individuals_number,cost=cost,start_time=start,end_time=end)
        if reserved_table:
            return Response(ReservationResponseSeralizer(reserved_table).data,status=status.HTTP_201_CREATED)
        

        return Response({"error":"internal server error"},status.HTTP_500_INTERNAL_SERVER_ERROR) 


extend_schema(request=ReservationRequestSerializer, responses=ReservationResponseSeralizer,tags=["reservation"])
class ReservationDetailView(ListAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationResponseSeralizer


    def get_queryset(self):

        queryset = super().get_queryset()

        queryset = queryset.filter(user=self.request.user)

        return queryset
    
    

