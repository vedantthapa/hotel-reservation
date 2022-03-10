from django.urls import path
from . views import *

urlpatterns = [
    path("hotels/", Hotel_list.as_view(), name="hotel_list"),
    path("booking/", Booking_List.as_view(), name="booking_list")
]
