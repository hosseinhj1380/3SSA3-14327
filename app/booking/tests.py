# tests/test_reservation_api.py

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from app.booking import values
from django.contrib.auth import get_user_model
from .models import Table

User = get_user_model()

class ReservationAPITestCase(APITestCase):

    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.profile_url = reverse("profile")
        self.reservation_url = reverse("reservation")
        self.reservation_detail_url = reverse("reservation-details")

        self.user_data = {
            "username": "testuser",
            "password": "strongpassword123",
            "phone":"09369455893",
            "email": "testuser@example.com"
        }

        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(self.login_url, {
            "username": self.user_data["username"],
            "password": self.user_data["password"]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.access_token = response.data["tokens"]["access"]
        
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        
        self.tables = []
        for i in range(1, 11):
            self.tables.append(Table.objects.create(name=f"Table {i}", seats=i + 1))  # seats: 2 to 11


    
    def test_reservation_start_before_opening_hour(self):
        now = timezone.now()
        start_time = now.replace(hour=values.RESTAURANT_OPENING_HOUR - 5, minute=0) + timedelta(days=1)
        end_time = start_time + timedelta(hours=2)
        
        data = {
            "individuals_number": 2,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat()
        }

        response = self.client.post(self.reservation_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_reservation(self):
        now = timezone.now()
        start_time = now + timedelta(days=1, hours=values.RESTAURANT_OPENING_HOUR + 1)
        end_time = start_time + timedelta(hours=2)

        data = {
            "individuals_number": 2,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat()
        }

        response = self.client.post(self.reservation_url, data, format="json")
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_406_NOT_ACCEPTABLE])
        if response.status_code == status.HTTP_201_CREATED:
            self.reservation_id = response.data["id"]  

    def test_list_reservations(self):
        response = self.client.get(self.reservation_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cancel_reservation(self):

        now = timezone.now()
        start_time = now + timedelta(days=1, hours=values.RESTAURANT_OPENING_HOUR + 1)
        end_time = start_time + timedelta(hours=2)

        data = {
            "individuals_number": 2,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat()
        }

        create_response = self.client.post(self.reservation_url, data, format="json")
        if create_response.status_code != status.HTTP_201_CREATED:
            self.skipTest("Reservation could not be created for cancellation test.")

        reservation_id = create_response.data["id"]

        cancel_url = reverse("cancel-reservation", args=[reservation_id])
        response = self.client.delete(cancel_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["detail"], "Reservation canceled successfully.")
