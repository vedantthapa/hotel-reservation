from rest_framework.serializers import ModelSerializer, ValidationError
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
        fields = ["hotel", "booking_id", "check_in", "check_out", "guest"]

    def create(self, validated_data):
        guest_data = validated_data.pop('guest')
        booking = Booking.objects.create(**validated_data)
        guest_set_serializer = self.fields['guest']
        for each in guest_data:
            each['booking'] = booking
        guest_set_serializer.create(guest_data)
        return booking

    def validate(self, data):
        if data['check_in'] > data['check_out']:
            raise ValidationError(
                {"check_out": "Check-out must occur after check-in date"})

        if not data['guest']:
            raise ValidationError({"guest": "Please enter atleast one guest"})

        bookings = Booking.objects.filter(hotel=data['hotel'])
        availability = []
        for booking in bookings:
            if booking.check_in > data['check_out'] or booking.check_out < data['check_in']:
                availability.append(True)
            else:
                availability.append(False)
        if not all(availability):
            raise ValidationError(
                f"{data['hotel']} is already booked for the specified dates! Please change the dates and try again.")

        return data
