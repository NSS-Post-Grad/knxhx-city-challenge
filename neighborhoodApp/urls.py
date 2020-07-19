from django.urls import path, include
from django.conf.urls import include
from neighborhoodApp.views import *
from neighborhoodApp.models import *


app_name = 'neighborhoodApp'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('search', search, name='search'),
    # path('', home, name='home'),
    path('', neighborhood_list, name='neighborhoods'),
    # path('home/', home, name='home'),
    path('home/', neighborhood_list, name='home'),
    path('neighborhoods/', neighborhood_list, name='neighborhoods'),
    path('neighborhoods/<int:org_id>', neighborhood_details, name='neighborhood'),
    path('residents/', resident_list, name='residents'),
    path('residents/<int:res_id>', resident_details, name='resident'),
    path('mailinglist/', mail_list, name='mailinglist'),
    path('neighborhood/form', neighborhood_form, name='neighborhood_form'),
    path('neighborhoods/<int:org_id>/resident_form', resident_form, name='resident_form'),
]



