# common/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('length/', views.length_converter, name='length_converter'),
    # Add more paths for other converters
]