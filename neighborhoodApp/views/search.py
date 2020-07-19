from django.shortcuts import render
from neighborhoodApp.models import Resident, Neighborhood_org

def search(request):

    if request.method == 'GET':

        form_data = request.GET

        if ('search-form' in form_data):

            if form_data['search'] == 'district':
                
                neighborhoods = Neighborhood_org.objects.filter(district=form_data['search-criteria'])

                context = {
                    "neighborhoods": neighborhoods
                }

            elif form_data['search'] == 'org_type':
                pass
            
            template = 'search_results.html'

            return render(request, template, context)

        else:

            template = 'search.html'

            return render(request, template)

