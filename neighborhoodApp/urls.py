from django.urls import path, include
from django.conf.urls import include
from neighborhoodApp.views import *
from neighborhoodApp.models import *


app_name = 'neighborhoodApp'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('search', search, name='search'),
    path('neighborhoods/', neighborhood_list, name='neighborhoods'),
    path('neighborhoods/<int:org_id>', neighborhood_details, name='neighborhood'),
]

