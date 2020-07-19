from django.urls import path, include
from django.conf.urls import include
from .views import *


app_name = 'neighborhoodApp'

urlpatterns = [
    path('', home, name='home'),
    path('neighborhoods/', neighborhood_list, name='neighborhoods'),
    path('neighborhood/form', neighborhood_form, name='neighborhood_form'),
]

