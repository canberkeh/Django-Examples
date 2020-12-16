from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [ 
    url(r'^index/$', crypto_index),
    url(r'^detail/$', crypto_detail),
    url(r'^create/$', crypto_create),
    url(r'^update/$', crypto_update),
    url(r'^delete/$', crypto_delete)

]
