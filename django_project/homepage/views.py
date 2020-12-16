from django.shortcuts import render

# Create your views here.

def homepage(request):
    context = {
        'isim':'berke',
    }
    return render(request, 'django_app/homepage.html', context)