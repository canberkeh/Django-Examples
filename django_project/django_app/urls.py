from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [ 
    url(r'^$', homepage),
    url('white_papers', white_papers),
    url('detail', crypto_detail),
]
