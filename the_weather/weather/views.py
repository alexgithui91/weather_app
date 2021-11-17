import os
import requests
from django.shortcuts import render
from dotenv import load_dotenv

# from the_weather.weather.forms import CityForm
from .models import City
from .forms import CityForm

# Load API Key
load_dotenv()
api_key = os.environ.get("API_KEY")

# Create your views here.
def index(request):
    url = (
        "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid="
        + api_key
    )

    cities = City.objects.all()  # return all the cities in the database

    if request.method == "post":
        form = CityForm(request.post)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json()

        weather = {
            "city": city,
            "temperature": city_weather["main"]["temp"],
            "description": city_weather["weather"][0]["description"],
            "icon": city_weather["weather"][0]["icon"],
        }

        weather_data.append(weather)

    context = {"weather_data": weather_data, "form": form}

    return render(request, "weather/index.html", context)
