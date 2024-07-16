from django.shortcuts import render

from weather.forms import CityForm


def index(request):
    form = CityForm()
    return render(request, 'weather/index.html', {'form': form})