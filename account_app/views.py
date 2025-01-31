from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def redirect_to_login(request):
    return redirect('account_app:login')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            role = form.cleaned_data.get('role')
            user = authenticate(request, email=email, password=password)
            if user is not None and user.role == role:
                login(request, user)
                if role == 'PATIENT':
                    return redirect('patient_app:patient_dashboard')
                elif role == 'DOCTOR':
                    return redirect('doctor_app:doctor_dashboard')
            else:
                form.add_error(None, "Invalid email, password, or role.")
    else:
        form = LoginForm()
    return render(request, 'account_app/login.html', {'form': form})

@login_required
def redirect_based_on_role(request):
    if request.user.role == 'PATIENT':
        return redirect('patient_app:patient_dashboard')
    elif request.user.role == 'DOCTOR':
        return redirect('doctor_app:doctor_dashboard')
    else:
        return redirect('account_app:login')
    
    