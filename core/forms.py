from django import forms

class WeatherFieldForm(forms.Form):
    city = forms.CharField(label='Your City Name -- e.g London', max_length=100)
    country = forms.CharField(label='Your Country Name -- e.g uk', max_length=20)
