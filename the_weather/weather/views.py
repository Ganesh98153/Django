from django.shortcuts import render
import requests
from weather.models import City
from weather.forms import Cityform




def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a68dffda8172c4053aa265e08256b4e9'
    if request.method == "POST":
        form = Cityform(request.POST)
        form.save()

    form = Cityform()

    cities = City.objects.all()

    weather_data = []

    try:

        for city in cities:

                 r= requests.get(url.format(city)).json()
                 city_weather = {
                'city' : city.name,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
                 }



        weather_data.append(city_weather)
    except KeyError:
        pass

    except Exception as e:
        pass

    context = {'weather_data': weather_data, 'form' : form}
    return render(request, 'weather/weather.html', context)



# Create your views here.
