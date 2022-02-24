import http.client
from celery import shared_task
from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')


@app.task
def get_weather_infromation(city, country):
    conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "8c64969435msh1a52448127e81f3p1f9de4jsn384ec693d495"
        }

    conn.request("GET", f"/weather?q={city}%2C{country}&lat=0&lon=0&callback=test&id=2172797&lang=null&units=imperial", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")