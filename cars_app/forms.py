from django import forms

class RentCarForm(forms.Form):
    user_login = forms.CharField(label='Your name', max_length=100)
    car_id = forms.CharField(max_length=100)
    duration_hours = forms.IntegerField(min_value=1, max_value=1000)
