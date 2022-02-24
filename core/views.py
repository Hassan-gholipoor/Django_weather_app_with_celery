import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import WeatherFieldForm
from .tasks import get_weather_infromation


def string_result_to_json(txt):
    res = txt.replace("test(", '')
    res = res.replace('"cod":200})', '"cod":200}')
    json_res = json.loads(res)
    
    return json_res

def get_weather_filed(request):
    if request.method == 'POST':
        form = WeatherFieldForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data['city'].capitalize()
            country = form.cleaned_data['country'].lower()
            result = get_weather_infromation.delay(city, country)
            res = result.get(timeout=1000)
            json_res = string_result_to_json(res)
            return JsonResponse(json_res)

    else:
        form = WeatherFieldForm()

    return render(request, 'weather.html', {'form': form})