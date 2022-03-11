from django.db import models
from datetime import datetime
import uuid


def generate_booking_id():
    return str(uuid.uuid4()).split("-")[-1]


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
    booking_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Booking confirmed!"

    def save(self, *args, **kwargs):
        if len(self.booking_id.strip(" ")) == 0:
            self.booking_id = generate_booking_id()

        super(Booking, self).save(*args, **kwargs)


class Guest(models.Model):
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='guest')
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=20)
    email = models.CharField(max_length=35)

    def __str__(self) -> str:
        return self.name
