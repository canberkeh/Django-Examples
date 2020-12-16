from django.shortcuts import render


# Create your views here.

def crypto_index(request):
    return render(request, 'django_app/crypto_index.html')
    
def crypto_detail(request):
    return render(request, 'django_app/crypto_detail.html')

def crypto_create(request):
    return render(request, 'django_app/crypto_create.html')

def crypto_update(request):
    return render(request, 'django_app/crypto_update.html')

def crypto_delete(request):
    return render(request, 'django_app/crypto_delete.html')

# def whitepapers(request):
#     return render(request, 'whitepapers/whitepapers.html')
