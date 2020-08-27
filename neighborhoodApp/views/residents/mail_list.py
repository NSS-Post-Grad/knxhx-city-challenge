import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from neighborhoodApp.models import Resident

@login_required
def mail_list(request):
    
    if request.method == 'GET':

        mail = Resident.objects.filter(is_subscribed = True)

        template = 'residents/mail_list.html'
        context = {
            'mail': mail
        }

        return render(request, template, context)

def mail_list_csv(request):

    if request.method == 'GET':

        mail = Resident.objects.filter(is_subscribed = True)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="mailing_list.csv'

        writer = csv.writer(response)

        column_names = ['First Name', 'Last Name', 'Address', 'City/State', 'Zipcode']
        rows = []

        for row in mail:
            rows.append([row.first_name, row.last_name, row.address_1, row.city_state, row.zip_code])

        writer.writerow(column_names)
        writer.writerows(rows)

        return response