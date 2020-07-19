from django.urls import path, include
from django.conf.urls import include
from .views import *


app_name = 'neighborhoodApp'

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('neighborhoods/', neighborhood_list, name='neighborhoods'),
    path('neighborhoods/<int:org_id>', neighborhood_details, name='neighborhood'),
    path('residents/', resident_list, name='residents'),
    path('residents/<int:res_id>', resident_details, name='resident'),
    path('mailinglist/', mail_list, name='mailinglist'),
    path('neighborhood/form', neighborhood_form, name='neighborhood_form'),
   
]

