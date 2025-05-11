from django.urls import path,include

from .views import ReservationsView,ReservationDetailView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns=[
    path('', ReservationsView.as_view(), name='reservation'),
    path('book', ReservationDetailView.as_view(), name='reservation-details'),

    
]


    
