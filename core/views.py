from django.shortcuts import render

from django.http import HttpResponse

def welcome(request):
    return HttpResponse('<h1>Welcome to Django!</h1>')

def greet(request):
    context = {
        'page_title': 'Dashboard',
        'greeting': 'Welcome to the Django Template Engine!',
        'user_name': 'hisham',
        'services': ['Nginx Reverse Proxy', 'Django WSGI Engine', 'PostgreSQL DB'],
    }

    return render(request, 'core/index.html', context)

def user_profile(request, username):
    context = {
        'page_title': f"{username.capitalize()}'s Profile",
        'username': username,
        'user_role': 'Administrator' if username.lower() == 'hisham' else 'Standard Member',
    }

    return render(request, 'core/profile.html', context)
