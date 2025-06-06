from django.urls import path,include

from .views import RegisterView, LoginView, ProfileView,TokenRefreshView


urlpatterns=[
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
]


    
