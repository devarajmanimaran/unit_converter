# common/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.common_converter, name="common_converter"),
]
