from django.shortcuts import render
# from curriculum.models import Background, Publication, Research
from teaching.models import Discipline
from website import models as models_website
from . import models

context = {}

def index(request):
    banner_skills = models_website.Banner_skill.objects.filter(status=True).first 
    biographie = models.Biography.objects.filter(status=True).first
    
    publications =models.Publication.objects.all()
    researches = models.Research.objects.all()

    # context['publications'] = publications
    # context['researches'] = researches

    site = models_website.Siteweb.objects.filter(status=True).first


    return render(request, 'curriculum/index.html', locals())


def skills(request):
    backgrounds_exp = models.Background.objects.filter(type='C')
    context['backgrounds_exp'] = backgrounds_exp
    backgrounds_act = models.Background.objects.filter(type='A')
    context['backgrounds_act'] = backgrounds_act
    return render(request, 'curriculum/skills.html', context)

def works(request):
    return render(request, 'curriculum/works.html')
