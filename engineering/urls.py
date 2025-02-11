# engineering/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('torque/', views.torque_converter, name='torque_converter'),
    # Add more paths for other engineering converters
]