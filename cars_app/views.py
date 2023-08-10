from django.shortcuts import render
from django.http import HttpResponse
from .models import Car


def cars_list(request):
    cars = Car.objects.order_by("-car_model")[:5]
    context = {"cars": cars}
    return render(request, "cars_list.html", context)
