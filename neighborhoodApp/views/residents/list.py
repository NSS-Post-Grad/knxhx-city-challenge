from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from neighborhoodApp.models import Neighborhood_org, Resident

@login_required
def resident_list(request):
    
    if request.method == 'GET':

        residents = Resident.objects.all()

        template = 'residents/list.html'
        context = {
            'residents': residents,
        }
        return render(request, template, context)

    elif request.method == 'POST':

        form_data = request.POST
        
        is_subscribed = False
        subscription = form_data['subscription']

        if (subscription == "yes"):
            is_subscribed = True

        org = Neighborhood_org(pk=form_data['neighborhood_org_id'])

        new_resident = Resident()
        new_resident.first_name = form_data['first_name']
        new_resident.last_name = form_data['last_name']
        new_resident.organization_position = form_data['organization_position']
        new_resident.email = form_data['email']
        new_resident.phone = form_data['phone']
        new_resident.address_1 = form_data['address_1']
        new_resident.address_2 = form_data['address_2']
        new_resident.city_state = form_data['city_state']
        new_resident.zip_code = form_data['zip_code']
        new_resident.is_subscribed = is_subscribed
        new_resident.neighborhood_org_id = org

        new_resident.save()

        return redirect(reverse('neighborhoodApp:residents'))