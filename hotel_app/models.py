from django.db import models
from django.conf import settings
from datetime import date, datetime


class Hotel(models.Model):
    name = models.CharField(max_length=25, null=False)
    email = models.CharField(max_length=35)
    city = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Guest(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=20)
    email = models.CharField(max_length=35)

    def __str__(self) -> str:
        return self.name


class Booking(models.Model):
    guest = models.ForeignKey(
        Guest, on_delete=models.CASCADE, related_name='guest')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in = models.DateField(default=datetime.now)
    check_out = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.guest} has booked {self.room} from {self.check_in} to {self.check_out}"

    def hotel_name(self):
        return self.hotel
