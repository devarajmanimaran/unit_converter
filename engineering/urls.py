# engineering/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.engineering_converter, name='engineering_converter'),
    # Add more paths for other engineering converters
]