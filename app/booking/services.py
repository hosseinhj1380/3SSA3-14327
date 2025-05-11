from .models import Reservation,Table
from django.db.transaction import atomic
from random import randint

def reserve_table(user,table,reserved_seats,cost,start_time,end_time):
    with atomic():
        tracking_code=randint(100000, 999999)
        return Reservation.objects.create(
            user=user,
            table=table,
            reserved_seats=reserved_seats,
            cost=cost,
            start_time=start_time,
            end_time=end_time,
            tracking_code=tracking_code
        )

