from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('account_app.urls')),
    path('doctor/', include('doctor_app.urls')),
    path('patient/', include('patient_app.urls')),
]