from django.db import models


# Create your models here.
class Car(models.Model):
    car_id = models.CharField(max_length=200, primary_key=True)
    license_number = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    year_of_production = models.IntegerField()
    odometer = models.FloatField()
    in_rent = models.BooleanField()
    car_cost = models.FloatField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()

    def __str__(self):
        return f'car_id: {self.car_id}, car_model: {self.manufacturer} {self.car_model}, in_rent: {self.in_rent}'


class User(models.Model):
    user_id = models.CharField(max_length=200, primary_key=True)
    user_phone = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    driver_license = models.CharField(max_length=200)
    debt = models.FloatField()

    def __str__(self):
        return f'user_id:{self.user_id}, name: {self.first_name} {self.last_name}'


class Deal(models.Model):
    deal_id = models.CharField(max_length=200, primary_key=True)
    duration_hours = models.IntegerField()
    cost = models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'deal_id: {self.deal_id}, user_id: {self.user_id}, cost: {self.cost}'

