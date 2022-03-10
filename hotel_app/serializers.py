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

    def create(self, validated_data):
        guest_data = validated_data.pop('guest')
        booking = Booking.objects.create(**validated_data)
        guest_set_serializer = self.fields['guest']
        for each in guest_data:
            each['booking'] = booking
        guest_set_serializer.create(guest_data)
        return booking
