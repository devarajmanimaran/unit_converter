# heat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fluids_converter, name='fluids_converter'),
    # Add more paths for other heat converters
]