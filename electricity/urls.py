# engineering/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.electricity_converter, name='electricity_converter'),
    # Add more paths for other engineering converters
]