from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from neighborhoodApp.models import Neighborhood_org, Resident

@login_required
def resident_details(request, res_id):
    
    if request.method == 'GET':

        resident = Resident.objects.get(pk=res_id)
        org = Neighborhood_org.objects.get(pk=resident.neighborhood_org_id_id)

        if resident.is_subscribed == True:
            subscribed = "*Subscribed to newsletter mailing list"
        else:
            subscribed = "*Not subscribed to newsletter mailing list"


        template = 'residents/details.html'
        context = {
            'org': org.name,
            'resident': resident,
            'subscribed': subscribed
        }

        return render(request, template, context)