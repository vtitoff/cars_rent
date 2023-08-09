from django.contrib import admin
from .models import Car, User, Deal, Manufacturer, CarModel

# Register your models here.
admin.site.register(Car)
admin.site.register(User)
admin.site.register(Deal)
admin.site.register(Manufacturer)
admin.site.register(CarModel)
