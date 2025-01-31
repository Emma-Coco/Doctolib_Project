from django.urls import path
from . import views

app_name = 'doctor_app'

urlpatterns = [
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]