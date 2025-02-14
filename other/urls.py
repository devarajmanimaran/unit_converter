# heat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.other_converter, name='other_converter'),
    # Add more paths for other heat converters
]