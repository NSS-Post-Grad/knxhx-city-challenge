from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from neighborhoodApp.models import Neighborhood_org, Resident


def neighborhood_details(request, org_id):

    residents = Resident.objects.filter(neighborhood_org_id=org_id)
    organization_positions = []

    for resident in residents:
        organization_positions.append(resident.organization_position)

    organization_positions = list(set(organization_positions))
    
    if request.method == 'GET':

        org = Neighborhood_org.objects.get(pk=org_id)
        loc_string = org.location
        address = loc_string.split(' ')
        address = '+'.join(address)

        template = 'neighborhoods/details.html'
        context = {
            'org': org,
            'address': address,
            'residents': residents,
            'organization_positions': organization_positions
        }

        return render(request, template, context)