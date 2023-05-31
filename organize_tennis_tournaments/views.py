from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'authentication/registration/register.html')
