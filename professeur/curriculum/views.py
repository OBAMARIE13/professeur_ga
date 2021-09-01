from django.shortcuts import render
from curriculum.models import Background, Publication, Research
from teaching.models import Discipline

context = {}

def index(request):
    
    publications = Publication.objects.all()
    researches = Research.objects.all()

    context['publications'] = publications
    context['researches'] = researches
    return render(request, 'curriculum/index.html', context)


def skills(request):
    backgrounds_exp = Background.objects.filter(type='C')
    context['backgrounds_exp'] = backgrounds_exp
    backgrounds_act = Background.objects.filter(type='A')
    context['backgrounds_act'] = backgrounds_act
    return render(request, 'curriculum/skills.html', context)

def works(request):
    return render(request, 'curriculum/works.html')
