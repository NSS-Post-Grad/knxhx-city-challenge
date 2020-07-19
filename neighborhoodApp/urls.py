from django.urls import path, include
from django.contrib import admin
from django.conf.urls import include
from neighborhoodApp.views import *
from neighborhoodApp.models import *


app_name = 'neighborhoodApp'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # path('admin/', admin.site.urls, name="admin"),
    path('logout/', logout_user, name='logout'),
    path('search', search, name='search'),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('neighborhoods/', neighborhood_list, name='neighborhoods'),
    path('neighborhoods/<int:org_id>', neighborhood_details, name='neighborhood'),
    path('residents/', resident_list, name='residents'),
    path('residents/<int:res_id>', resident_details, name='resident'),
    path('mailinglist/', mail_list, name='mailinglist'),
    path('neighborhood/form', neighborhood_form, name='neighborhood_form'),
    path('neighborhoods/<int:org_id>/resident_form', resident_form, name='resident_form'),
]



