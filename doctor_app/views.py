from django.shortcuts import render, redirect
from .forms import CustomSignUpForm

def Doctor_view(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test')  # Assure-toi que 'test' est bien défini dans urls.py
        else:
            print(form.errors)  # Affiche les erreurs du formulaire dans la console
    else:
        form = CustomSignUpForm()
    
    return render(request, 'Docteur.html', {'form': form})
