from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from neighborhoodApp.models import Neighborhood_org


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