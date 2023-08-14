from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Car
from .forms import RentCarForm

def cars_list(request):
    cars = Car.objects.order_by("-car_model")[:5]
    form = RentCarForm()
    context = {"cars": cars, "form": form}
    return render(request, "cars_list.html", context)


def rent_car(request):
    if request.method == 'POST':
        form = RentCarForm(request.POST)
        if form.is_valid():
            print(f"FORM {form.cleaned_data}")
            return HttpResponseRedirect('/app/thanks')
    return cars_list(request)
