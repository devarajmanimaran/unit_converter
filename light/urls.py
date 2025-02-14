# heat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.light_converter, name='light_converter'),
    # Add more paths for other heat converters
]