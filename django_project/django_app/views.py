from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'django_app/index.html')

def whitepapers(request):
    return render(request, 'whitepapers/whitepapers.html')
