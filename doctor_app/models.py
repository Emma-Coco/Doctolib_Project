from django.contrib.auth.models import AbstractUser
from django.db import models

class Doctor(AbstractUser):
    telephone = models.CharField(max_length=15, null=True, blank=True)
    license = models.CharField(max_length=15, primary_key=True, unique=True)
    genre = models.CharField(max_length=10, null=True, blank=True)
    sys_created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sys_updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    specialty = models.CharField(max_length=15, null=True, blank=True)
    class Meta:
        db_table = 'app_ecg_Doctor'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='doctor_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='doctor_permissions',
        blank=True
    )

    def __str__(self):
        return self.first_name
