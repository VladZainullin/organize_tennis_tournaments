from django.shortcuts import render


def index(request):
    return render(request, 'organizers/index.html')
