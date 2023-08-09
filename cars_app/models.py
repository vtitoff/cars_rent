from django.db import models
import uuid
from enum import Enum


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.manufacturer} {self.name}"


class Car(models.Model):
    car_id = models.CharField(max_length=200, primary_key=True, default=uuid.uuid4())
    license_number = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year_of_production = models.IntegerField()
    odometer = models.FloatField()
    in_rent = models.BooleanField()
    car_cost = models.FloatField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()

    def __str__(self):
        return f"{self.car_model} {self.license_number}, in_rent: {self.in_rent}, car_id: {self.car_id}"


class User(models.Model):
    user_id = models.CharField(max_length=200, primary_key=True, default=uuid.uuid4())
    user_phone = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    driver_license = models.CharField(max_length=50)
    debt = models.FloatField()

    def __str__(self):
        return f"user_id:{self.user_id}, name: {self.first_name} {self.last_name}"


class Deal(models.Model):
    STATUSES = (
        ("NEW", "new"),
        ("IN_PROGRESS", "in_progress"),
        ("CANCELLED", "cancelled"),
        ("FINISHED", "finished"),
    )

    deal_id = models.CharField(max_length=200, primary_key=True, default=uuid.uuid4())
    duration_hours = models.IntegerField()
    cost = models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUSES, default="NEW")

    def __str__(self):
        return f"deal_id: {self.deal_id}, user_id: {self.user_id}, cost: {self.cost}"
