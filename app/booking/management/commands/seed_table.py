from django.core.management.base import BaseCommand
from app.booking.models import Table  # Adjust path as needed
import random

class Command(BaseCommand):
    help = 'Seed the database with 10 table entries'

    def handle(self, *args, **kwargs):
        Table.objects.all().delete()  # Optional: clear existing tables
        for i in range(10):
            Table.objects.create(
                name=f"Table {i+1}",
                seats=random.randint(4, 10)
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded 10 tables'))
