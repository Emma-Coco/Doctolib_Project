


# app_ecg/views.py
from django.shortcuts import render, redirect
from .forms import CustomSignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de connexion ou une autre page après l'inscription
    else:
        form = CustomSignUpForm()
    
    return render(request, 'signup.html', {'form': form})

