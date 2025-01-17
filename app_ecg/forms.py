from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomSignUpForm(UserCreationForm):
    nom = forms.CharField(max_length=150, label="Nom", required=True)
    prenom = forms.CharField(max_length=150, label="Prénom", required=True)
    mail = forms.EmailField(label="Email", required=True)
    telephone = forms.CharField(max_length=15, label="Téléphone", required=True)
    numero_securite_social = forms.CharField(max_length=15, label="Numéro de Sécurité Sociale", required=True)
    birth_date = forms.DateField(label="Date de Naissance", widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    genre = forms.ChoiceField(
        choices=[('M', 'Masculin'), ('F', 'Féminin'), ('O', 'Autre')],
        label="Genre",
        required=True
    )
    nom_medecin_traitant = forms.CharField(max_length=150, label="Nom du Médecin Traitant", required=True)
    code_postal = forms.CharField(max_length=10, label="Code Postal", required=True)
    ville = forms.CharField(max_length=100, label="Ville", required=True)
    rue = forms.CharField(max_length=200, label="Rue", required=True)
    sys_created_at = forms.DateTimeField(label="Date de Création", required=False, widget=forms.HiddenInput())
    sys_updated_at = forms.DateTimeField(label="Date de Mise à Jour", required=False, widget=forms.HiddenInput())

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'email', 'password1', 'password2', 
            'nom', 'prenom', 'mail', 'telephone', 'numero_securite_social', 
            'birth_date', 'genre', 'nom_medecin_traitant', 
            'code_postal', 'ville', 'rue', 
            'sys_created_at', 'sys_updated_at'
        )
        labels = {
            'username': 'Nom d’utilisateur',
            'email': 'Adresse email',
            'password1': 'Mot de passe',
            'password2': 'Confirmez votre mot de passe',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        # Ajoutez les champs supplémentaires à l'objet utilisateur si nécessaire
        user.nom = self.cleaned_data.get('nom')
        user.prenom = self.cleaned_data.get('prenom')
        user.mail = self.cleaned_data.get('mail')
        user.telephone = self.cleaned_data.get('telephone')
        user.numero_securite_social = self.cleaned_data.get('numero_securite_social')
        user.birth_date = self.cleaned_data.get('birth_date')
        user.genre = self.cleaned_data.get('genre')
        user.nom_medecin_traitant = self.cleaned_data.get('nom_medecin_traitant')
        user.code_postal = self.cleaned_data.get('code_postal')
        user.ville = self.cleaned_data.get('ville')
        user.rue = self.cleaned_data.get('rue')
        user.sys_created_at = self.cleaned_data.get('sys_created_at') or None
        user.sys_updated_at = self.cleaned_data.get('sys_updated_at') or None

        if commit:
            user.save()
        return user
