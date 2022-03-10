from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Guest, Hotel, Booking


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ("name", "email", "city")


class GuestSerializer(ModelSerializer):
    class Meta:
        model = Guest
        fields = ("name", "age", "email")


class BookingSerializer(ModelSerializer):
    guest = GuestSerializer(many=True)

    class Meta:
        model = Booking
        fields = ["hotel", "check_in", "check_out", "guest"]
