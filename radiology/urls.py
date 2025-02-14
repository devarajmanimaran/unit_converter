# heat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.radiology_converter, name='radiology_converter'),
    # Add more paths for other heat converters
]