from django.urls import path, include
from django.conf.urls import include
from .views import *


app_name = 'neighborhoodApp'

urlpatterns = [
path('neighborhoods/', neighborhood_list, name='neighborhoods'),
path('neighborhoods/<int:org_id>', neighborhood_details, name='neighborhood'),
]

