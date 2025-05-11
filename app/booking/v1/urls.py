from django.urls import path,include

from .views import BookView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns=[
    path('', BookView.as_view(), name='Booking'),
    
]


    
