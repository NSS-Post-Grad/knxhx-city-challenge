from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from neighborhoodApp.models import Neighborhood_org, Resident

@login_required
def resident_list(request):
    
    if request.method == 'GET':

        residents = Resident.objects.all()

        template = 'residents/list.html'
        context = {
            'residents': residents
        }
        return render(request, template, context)