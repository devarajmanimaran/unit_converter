"""
URL configuration for unit_converter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# unit_converter/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('engineering/', include('engineering.urls')),
    path('heat/', include('heat.urls')),
    path('fluids/', include('fluids.urls')),
    path('light/', include('light.urls')),
    path('magnetism/', include('magnetism.urls')),
    path('electricity/', include('electricity.urls')),
    path('radiology/', include('radiology.urls')),
    path('other/', include('other.urls')),
    path('', include('core.urls')),
]