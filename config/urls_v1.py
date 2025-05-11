
from django.urls import path, include
from django.urls import path


urlpatterns = [
    path("account/",include("app.account.v1.urls"), name="user"),
    path("reservation/",include("app.booking.v1.urls"), name="book"),

]

