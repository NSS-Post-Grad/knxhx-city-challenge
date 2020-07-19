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