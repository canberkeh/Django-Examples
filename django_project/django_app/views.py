from django.shortcuts import render
from .models import Crypto

# Create your views here.

def homepage(request):
    return render(request, 'django_app/homepage.html')

def white_papers(request):
    crypto_models = Crypto.objects.all()
    return render(request, 'django_app/white_papers.html', {'Cryptos': crypto_models})

def crypto_detail(request):
    crypto_details = Crypto.objects.values('content') # NOT WORKING
    return render(request, 'django_app/crypto_detail.html', {'Cryptos': crypto_detail})

# def whitepapers(request):
#     return render(request, 'whitepapers/whitepapers.html')
