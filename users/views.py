# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserRegisterForm  

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('users:login')  
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.xhtml', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('candidates:index') 
        else:
            messages.error(request, "Login failed. Please check your username and password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.xhtml', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('users:login')  
