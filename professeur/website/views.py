import re
from django.shortcuts import render
from . import models
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    banner = models.Banner.objects.filter(status=True).first
    return render(request, 'index.html', locals())

@csrf_exempt
def checkup(request):
    success = True
    text = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')

        if email.isspace() or email == '' or name.isspace() or name == '' or message.isspace() or message == '':
            success = False
            text = 'Veuillez remplir les champs vides'
        elif not re.fullmatch('(\w\.?)+@(\w\.?)+\.[A-Za-z]{2,3}', email):
            success = False
            text = 'Veuillez saisir un email valide'
        elif not re.fullmatch("[A-Za-z'éèëöüïäû ]+", name):
            success = False
            text = 'Veuillez saisir un nom valide'
        else:
            contact = models.Contact(name=name, message=message, email=email)
            contact.save()
            text = 'Votre message a bien été enregistré'

    datas = {
        'success':success,
        'text':text
    }

    return JsonResponse(datas, safe=False)
