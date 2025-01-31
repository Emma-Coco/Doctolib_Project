from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'account_app'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='account_app:login'), name='home'),  # Redirige vers la page de connexion
    path('login/', views.login_view, name='login'),
    path('redirect/', views.redirect_based_on_role, name='redirect'),
]