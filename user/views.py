from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect('index')
    return render(request, 'auth/registration.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'auth/log_in.html')


def log_out(request):
    logout(request)
    return redirect('index')
