from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from neighborhoodApp.models import Neighborhood_org


def neighborhood_details(request, org_id):
    
    if request.method == 'GET':

        org = Neighborhood_org.objects.get(pk=org_id)
        loc_string = org.location
        address = loc_string.split(' ')
        address = '+'.join(address)

        template = 'neighborhoods/details.html'
        context = {
            'org': org,
            'address': address
        }

        return render(request, template, context)