# app_ecg/urls.py
# app_ecg/urls.py

from django.urls import path
from .views import Doctor_view

urlpatterns = [
    path('Doctor/', Doctor_view, name='Doctor'),
]


