from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response


class Hotel_list(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class Booking_List(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            booking_id = serializer.data.pop('booking_id')
            return Response(f"Your confirmation number is: {booking_id}", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
