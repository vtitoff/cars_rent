from django.urls import path

from . import views

app_name = "cars_app"
urlpatterns = [
    path("cars", views.cars_list, name="cars_list"),
    path("thanks", views.rent_car, name="thanks"),
]
