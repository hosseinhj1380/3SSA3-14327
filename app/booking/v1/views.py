
from app.booking import selectors,services
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.utils.dateparse import parse_datetime
from .serializer import BookingRequestSerializer,BookingResponseSeralizer
from app.booking.helper import best_fit_table
from drf_spectacular.utils import extend_schema
from app.booking.models import Reservation,Table

class BookView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(request=BookingRequestSerializer, responses=BookingResponseSeralizer,tags=["booking"])
    def post(self, request):
        serializer = BookingRequestSerializer(data=request.data)
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
            return Response(BookingResponseSeralizer(reserved_table).data,status=status.HTTP_201_CREATED)
        

        return Response({"error":"internal server error"},status.HTTP_500_INTERNAL_SERVER_ERROR) 


        
       

