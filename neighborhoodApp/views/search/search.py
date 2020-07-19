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
                search = "active organizations"

                context = {
                    "neighborhoods": neighborhoods,
                    "search": search
                }

                template = 'search/search_results_neighborhood.html'

            elif value == "inactive":

                neighborhoods = Neighborhood_org.objects.filter(is_active=False)
                search = "inactive organizations"

                context = {
                    "neighborhoods": neighborhoods,
                    "search": search
                }

                template = 'search/search_results_neighborhood.html'

            else:

                context = {
                    "value": value,
                }
                
                template = 'search/search_criteria.html'

            return render(request, template, context)

        elif ('search-criteria-form' in form_data):

                search_criteria = form_data['search-criteria']

                if (form_data['search-criteria-form'] == 'district'):
                    
                    neighborhoods = Neighborhood_org.objects.filter(district=form_data['search-criteria'])

                    search = "district"

                    context = {
                        "neighborhoods": neighborhoods,
                        "search_criteria": search_criteria,
                        "search": search
                    }

                    template = 'search/search_results_neighborhood.html'

                    return render(request, template, context)

                elif (form_data['search-criteria-form'] == 'org_type'):
                    
                    neighborhoods = Neighborhood_org.objects.filter(org_type=form_data['search-criteria'])

                    search = "neighborhood organization type -"

                    context = {
                        "neighborhoods": neighborhoods,
                        "search_criteria": search_criteria,
                        "search": search
                    }

                    template = 'search/search_results_neighborhood.html'

                    return render(request, template, context)

                elif (form_data['search-criteria-form'] == 'neighborhood_name'):
                    
                    neighborhoods = Neighborhood_org.objects.filter(name__icontains=form_data['search-criteria'])

                    search = "neighborhood organization name -"

                    context = {
                        "neighborhoods": neighborhoods,
                        "search_criteria": search_criteria,
                        "search": search
                    }

                    template = 'search/search_results_neighborhood.html'

                    return render(request, template, context)

                elif (form_data['search-criteria-form'] == 'day'):
                    
                    neighborhoods = Neighborhood_org.objects.filter(day=form_data['search-criteria'])

                    search = "meeting day -"

                    context = {
                        "neighborhoods": neighborhoods,
                        "search_criteria": search_criteria,
                        "search": search
                    }

                    template = 'search/search_results_neighborhood.html'

                    return render(request, template, context)

                elif (form_data['search-criteria-form'] == 'resident_first_name'):
                    
                    residents = Resident.objects.filter(first_name__icontains=form_data['search-criteria'])

                    search = "resident first name -"

                    context = {
                        "residents": residents,
                        "search_criteria": search_criteria,
                        "search": search
                    }

                    template = 'search/search_results_resident.html'

                    return render(request, template, context)

                elif (form_data['search-criteria-form'] == 'resident_last_name'):
                    
                    residents = Resident.objects.filter(last_name__icontains=form_data['search-criteria'])

                    search = "resident last name-"

                    context = {
                        "residents": residents,
                        "search_criteria": search_criteria,
                        "search": search
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

