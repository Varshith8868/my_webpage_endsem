# app39/urls.py
from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the home view
]
