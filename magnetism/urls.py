# heat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.magnetism_converter, name='magnetism_converter'),
    # Add more paths for other heat converters
]