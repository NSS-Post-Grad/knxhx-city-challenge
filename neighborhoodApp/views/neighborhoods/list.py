from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from neighborhoodApp.models import Neighborhood_org
from datetime import datetime

def neighborhood_list(request):
    
    if request.method == 'GET':

        orgs = Neighborhood_org.objects.all()
        areas = ["North", "South", "East", "West"]

        template = 'neighborhoods/list.html'
        context = {
            'orgs': orgs,
            'areas': areas
        }
        return render(request, template, context)

    elif request.method == 'POST':

        form_data = request.POST
        is_active = False
        meeting = form_data['meeting']
        if (meeting == "yes"):
            is_active = True


        new_neighborhood = Neighborhood_org()
        new_neighborhood.name = form_data['name']
        new_neighborhood.org_type = form_data['org_type']
        new_neighborhood.email = form_data['email']
        new_neighborhood.boundary = form_data['boundary']
        new_neighborhood.website = form_data['website']
        new_neighborhood.facebook = form_data['facebook']
        new_neighborhood.district = form_data['district']
        new_neighborhood.notes = form_data['notes']
        new_neighborhood.location = form_data['location']
        new_neighborhood.time = form_data['time']
        new_neighborhood.day = form_data['day']
        new_neighborhood.week = form_data['week']
        new_neighborhood.frequency = form_data['frequency']
        new_neighborhood.last_updated = datetime.now()
        new_neighborhood.is_active = is_active
              
        new_neighborhood.save()

        return redirect(reverse('neighborhoodApp:neighborhoods'))
