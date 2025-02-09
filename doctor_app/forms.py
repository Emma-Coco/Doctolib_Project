from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from doctor_app.models import Doctor

class CustomSignUpForm(UserCreationForm):
   
    telephone = forms.CharField(max_length=15, label="Téléphone", required=True)
    license = forms.CharField(max_length=15, label="Numéro RPPS", required=True)
    specialty = forms.CharField(max_length=15, label="specialty", required=True)
    genre = forms.ChoiceField(
        choices=[('M', 'Masculin'), ('F', 'Féminin'), ('O', 'Autre')],
        label="Genre",
        required=True
    )
    sys_created_at = forms.DateTimeField(label="Date de Création", required=False, widget=forms.HiddenInput())
    sys_updated_at = forms.DateTimeField(label="Date de Mise à Jour", required=False, widget=forms.HiddenInput())

    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'email', 'password1', 'password2',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        # Ajoutez les champs supplémentaires à l'objet utilisateur si nécessaire
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.telephone = self.cleaned_data.get('telephone')
        user.license = self.cleaned_data.get('numero_RPPS')
        user.genre = self.cleaned_data.get('genre')
        user.specialty = self.cleaned_data.get('specialty')
        user.sys_created_at = self.cleaned_data.get('sys_created_at') or None
        user.sys_updated_at = self.cleaned_data.get('sys_updated_at') or None

        if commit:
            user.save()
        return user
