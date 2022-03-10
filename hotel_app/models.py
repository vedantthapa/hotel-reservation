from django.db import models
from django.conf import settings
from datetime import date, datetime


class Hotel(models.Model):
    name = models.CharField(max_length=25, null=False, primary_key=True)
    email = models.CharField(max_length=35)
    city = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in = models.DateField(default=datetime.now)
    check_out = models.DateField(default=datetime.now)

    def __str__(self):
        return f"Booking confirmed!"

    def hotel_name(self):
        return self.hotel


class Guest(models.Model):
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='guest')
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=20)
    email = models.CharField(max_length=35)

    def __str__(self) -> str:
        return self.name
