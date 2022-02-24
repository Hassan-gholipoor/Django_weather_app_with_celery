from django.urls import path
from .views import get_weather_filed
app_name = 'weather'

urlpatterns = [
    path('', get_weather_filed, name='get_weather')
]