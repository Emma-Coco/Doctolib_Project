from django.urls import path
from . import views

app_name = 'patient_app'

urlpatterns = [
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
]