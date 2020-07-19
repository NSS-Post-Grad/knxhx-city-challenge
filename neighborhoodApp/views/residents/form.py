import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from neighborhoodApp.models import Neighborhood_org

@login_required
def resident_form(request, org_id):

    org = Neighborhood_org.objects.get(pk=org_id)
    city_state = "Knoxville, TN"

    if request.method == 'GET':

        context = {
            "org": org,
            "city_state": city_state
        }

        template = 'residents/form.html'

        return render(request, template, context)