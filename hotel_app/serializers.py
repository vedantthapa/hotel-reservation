from rest_framework.serializers import ModelSerializer
from .models import Guest, Hotel, Booking


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ("name", "email", "city")
