from . import views
from django.urls import path

app_name = 'weather'

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/', views.weather, name='weather'),
]