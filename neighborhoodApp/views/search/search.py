from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from neighborhoodApp.models import Resident, Neighborhood_org

@login_required
def search(request):

    if request.method == 'GET':

        form_data = request.GET

        if ('search-form' in form_data):

            value = form_data['search']

            if value == "active":

                neighborhoods = Neighborhood_org.objects.filter(is_active=True)

                context = {
                    "neighborhoods": neighborhoods
                }

                template = 'search/search_results_neighborhood.html'

            elif value == "inactive":

                neighborhoods = Neighborhood_org.objects.filter(is_active=False)

                context = {
                    "neighborhoods": neighborhoods
                }

                template = 'search/search_results_neighborhood.html'

            else:

                # all_neighborhoods = Neighborhood_org.objects.all()
                # organization_types = []

                # for neighborhood in all_neighborhoods:
                #     organization_types.append(neighborhood.org_type)

                # organization_types = list(set(organization_types))

                context = {
                    "value": value,
                    # "organization_types": organization_types
                }
                
                template = 'search/search_criteria.html'

            return render(request, template, context)

        elif ('search-criteria-form' in form_data):

                if (form_data['search-criteria-form'] == 'district'):
                    
                    neighborhoods = Neighborhood_org.objects.filter(district=form_data['search-criteria'])

                    context = {
                        "neighborhoods": neighborhoods
                    }

                    template = 'search/search_results_neighborhood.html'

                    return render(request, template, context)

                elif (form_data['search-criteria-form'] == 'org_type'):
                    
                    neighborhoods = Neighborhood_org.objects.filter(org_type=form_data['search-criteria'])

                    context = {
                        "neighborhoods": neighborhoods
                    }

                    template = 'search/search_results_neighborhood.html'

                    return render(request, template, context)

                elif (form_data['search-criteria-form'] == 'neighborhood_name'):
                    
                    neighborhoods = Neighborhood_org.objects.filter(name__icontains=form_data['search-criteria'])

                    context = {
                        "neighborhoods": neighborhoods,
                    }

                    template = 'search/search_results_neighborhood.html'

                    return render(request, template, context)

                elif (form_data['search-criteria-form'] == 'day'):
                    
                    neighborhoods = Neighborhood_org.objects.filter(day=form_data['search-criteria'])

                    context = {
                        "neighborhoods": neighborhoods
                    }

                    template = 'search/search_results_neighborhood.html'

                    return render(request, template, context)

                elif (form_data['search-criteria-form'] == 'resident_first_name'):
                    
                    residents = Resident.objects.filter(first_name__icontains=form_data['search-criteria'])

                    context = {
                        "residents": residents
                    }

                    template = 'search/search_results_resident.html'

                    return render(request, template, context)

                elif (form_data['search-criteria-form'] == 'resident_last_name'):
                    
                    residents = Resident.objects.filter(last_name__icontains=form_data['search-criteria'])

                    context = {
                        "residents": residents
                    }

                    template = 'search/search_results_resident.html'

                    return render(request, template, context)

        else:

            template = 'search/search.html'

            return render(request, template)


# @login_required
# def search(request):

#     if request.method == 'GET':

#         form_data = request.GET

#         if ('search-form' in form_data):

#             if form_data['search'] == 'district':
                
#                 neighborhoods = Neighborhood_org.objects.filter(district=form_data['search-criteria'])

#                 context = {
#                     "neighborhoods": neighborhoods
#                 }

#             elif form_data['search'] == 'org_type':
                
#                 neighborhoods = Neighborhood_org.objects.filter(org_type=form_data['search-criteria'])

#                 context = {
#                     "neighborhoods": neighborhoods
#                 }

#             elif form_data['search'] == 'neighborhood_name':
                
#                 neighborhoods = Neighborhood_org.objects.filter(name=form_data['search-criteria'])

#                 context = {
#                     "neighborhoods": neighborhoods
#                 }

#             elif form_data['search'] == 'day':
                
#                 neighborhoods = Neighborhood_org.objects.filter(day=form_data['search-criteria'])

#                 context = {
#                     "neighborhoods": neighborhoods
#                 }

#             elif form_data['search'] == 'active':
                
#                 neighborhoods = Neighborhood_org.objects.filter(is_active=True)

#                 context = {
#                     "neighborhoods": neighborhoods
#                 }

#             elif form_data['search'] == 'inactive':
                
#                 neighborhoods = Neighborhood_org.objects.filter(is_active=False)

#                 context = {
#                     "neighborhoods": neighborhoods
#                 }

#             elif form_data['search'] == 'resident_first_name':
                
#                 residents = Resident.objects.filter(first_name=form_data['search-criteria'])

#                 context = {
#                     "residents": residents
#                 }

#             elif form_data['search'] == 'resident_last_name':
                
#                 residents = Resident.objects.filter(last_name=form_data['search-criteria'])

#                 context = {
#                     "residents": residents
#                 }

            
#             template = 'search_results.html'

#             return render(request, template, context)

#         else:

#             template = 'search.html'

#             return render(request, template)

