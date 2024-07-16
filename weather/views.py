from django.shortcuts import render

from weather.forms import CityForm


def index(request):
    form = CityForm()
    return render(request, 'weather/index.html', {'form': form})

def weather(request):
    form = CityForm()
    return render(request, 'weather/weather.html', {'form': form})