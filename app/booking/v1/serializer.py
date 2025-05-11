from rest_framework import serializers
from app.booking.models import Reservation
from django.utils import timezone
from datetime import timedelta
from app.booking import values

class BookingRequestSerializer(serializers.Serializer):
    individuals_number= serializers.IntegerField(min_value=1)
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

    def validate(self, data):
        start = data['start_time']
        end = data['end_time']
        now = timezone.now()

        if start <= now:
            raise serializers.ValidationError("Start time must be in the future.")
        if end <= now:
            raise serializers.ValidationError("End time must be in the future.")
        if end <= start:
            raise serializers.ValidationError("End time must be after start time.")

        duration = end - start
        if duration < timedelta(hours=values.MIN_RESERVATION_HOURS):
            raise serializers.ValidationError(
                f"Reservation must be at least {values.MIN_RESERVATION_HOURS} hour(s)."
            )
        if duration > timedelta(hours=values.MAX_RESERVATION_HOURS):
            raise serializers.ValidationError(
                f"Reservation cannot exceed {values.MAX_RESERVATION_HOURS} hour(s)."
            )

        # Time boundary check (opening/closing hours)
        opening_hour = values.RESTAURANT_OPENING_HOUR
        closing_hour = values.RESTAURANT_CLOSING_HOUR

        if not (opening_hour <= start.hour < closing_hour):
            raise serializers.ValidationError(
                f"Reservation must start between {opening_hour}:00 and {closing_hour - 1}:59."
            )
        if not (opening_hour < end.hour <= closing_hour):
            raise serializers.ValidationError(
                f"Reservation must end between {opening_hour + 1}:00 and {closing_hour}:00."
            )

        return data



class BookingResponseSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields ='__all__'