from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class Table(models.Model):
    name = models.CharField(blank=True,null=True)
    seats = models.IntegerField(
        default=4, validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def __str__(self):
        return f"{self.id}-seats:{self.seats}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, related_name="reservations", on_delete=models.CASCADE)
    reserved_seats = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    tracking_code = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(start_time__lt=models.F('end_time')), name='valid_time_range')
        ]

    def __str__(self):
        return f"{self.user.name}-seats:{self.reserved_seats}-table:{self.table.id}"

