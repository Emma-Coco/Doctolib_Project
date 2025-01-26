from django.contrib.auth.models import AbstractUser
from django.db import models

class Patient(AbstractUser):
    telephone = models.CharField(max_length=15, null=True, blank=True)
    numero_securite_social = models.CharField(max_length=15, primary_key=True, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=10, null=True, blank=True)
    nom_medecin_traitant = models.CharField(max_length=150, null=True, blank=True)
    code_postal = models.CharField(max_length=10, null=True, blank=True)
    ville = models.CharField(max_length=100, null=True, blank=True)
    rue = models.CharField(max_length=200, null=True, blank=True)
    sys_created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sys_updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        db_table = 'app_ecg_patient'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )

    def __str__(self):
        return self.first_name
