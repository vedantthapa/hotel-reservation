from django.urls import path
from . import views

urlpatterns = [
    path("hotels/", views.Hotel_list.as_view(), name="hotel_list")
]
