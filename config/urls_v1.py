
from django.urls import path, include
from django.urls import path


urlpatterns = [
    path("user/",include("app.users.v1.urls"), name="user"),
    path("book/",include("app.booking.v1.urls"), name="book"),

]

