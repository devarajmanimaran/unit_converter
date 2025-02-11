# heat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('thermal-conductivity/', views.thermal_conductivity_converter, name='thermal_conductivity_converter'),
    # Add more paths for other heat converters
]