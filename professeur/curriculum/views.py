from django.shortcuts import get_object_or_404, render
from django.http.response import JsonResponse # 
from django.shortcuts import render
from website import models as models_website
from curriculum import models as models_curriculum


def index(request):
    abouts = models_curriculum.About.objects.filter(status=True).first()
    is_index = True
    gallerie = models_website.Gallerie.objects.filter(status=True).first()
    return render(request, 'curriculum/index.html')


def skills(request):
    return render(request, 'curriculum/skills.html')

def works(request):
    return render(request, 'curriculum/works.html')



def postdata(request):
    
    succes = False
    message = ''

    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    if not name or name.isspace():
        message = 'Veuillez entrer un nom valide'

    elif not email or email.isspace():
        message = 'Veuillez entrer un email valide'

    elif not message or message.isspace():
        message = 'Veuillez entrer un message valide'

    else:
        succes, message = True , 'message envoyé'
        contacts = models.Contact(name=name , email=email, message= message)
        contacts.save()


    datas = {
        'succes': succes,
        'message': message,

    }
    return JsonResponse(datas, safe=False)