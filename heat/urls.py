# heat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.heat_converter, name='heat_converter'),
    # Add more paths for other heat converters
]