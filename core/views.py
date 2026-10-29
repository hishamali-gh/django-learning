from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if not user:
            err_msg = 'Invalid username or password! Please try again.'

            return render(request, 'core/login.html', {'error': err_msg})

        login(request, user)

        return redirect('dashboard')

    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)

    return redirect('login')

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'core/dashboard.html')
