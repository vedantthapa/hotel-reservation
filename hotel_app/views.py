from .models import *
from .serializers import *
from datetime import datetime
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response


class Hotel_list(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_queryset(self):
        data = self.request.data
        if ("check_in" in data) and ("check_out" in data):
            bookings = Booking.objects.all()
            check_in = datetime.strptime(data['check_in'], "%Y-%m-%d").date()
            check_out = datetime.strptime(data['check_out'], "%Y-%m-%d").date()

            booked_hotels = []

            for booking in bookings:
                if booking.check_in < check_in:
                    if booking.check_out < check_in:
                        continue
                    else:
                        booked_hotels.append(booking.hotel.name)
                else:
                    if check_out < booking.check_in:
                        continue
                    else:
                       booked_hotels.append(booking.hotel.name)

            return Hotel.objects.filter(~Q(name__in=booked_hotels))

        else:
            return Hotel.objects.all()


class Booking_List(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def post(self, request, format=None):
        print(request.data)
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            booking_id = serializer.data.pop('booking_id')
            return Response(f"Booking confirmed with ID: {booking_id}", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
