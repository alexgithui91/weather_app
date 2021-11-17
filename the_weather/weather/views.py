import os
import requests
from django.shortcuts import render
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.environ.get("API_KEY")

# Create your views here.
def index(request):
    url = (
        "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid="
        + api_key
    )
    city = "Las Vegas"

    city_weather = requests.get(url.format(city)).json()

    print(city_weather)

    return render(request, "weather/index.html")
