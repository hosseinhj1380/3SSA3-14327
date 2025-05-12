from django.urls import path,include

from .views import ReservationsView,ReservationDetailView,CancelReservationView



urlpatterns=[
    path('', ReservationsView.as_view(), name='reservation'),
    path('book', ReservationDetailView.as_view(), name='reservation-details'),
    path('<int:reservation_id>/cancel/', CancelReservationView.as_view(), name='cancel-reservation'),


    
]


    
