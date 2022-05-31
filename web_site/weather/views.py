import requests
from django.shortcuts import render


def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=34ad35266692aa8c9067dafe37b731b9'
    city = 'Ekaterinburg'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"],
        'humid': res["main"]["humidity"],
        'wind': res["wind"]["speed"],
    }
    context = {
        'info': city_info
    }
    return render(request, 'weather/index.html', context)