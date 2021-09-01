from django.shortcuts import render
from teaching.models import Discipline, Training

context = {}

def courses(request):
    return render(request, 'teaching/courses.html')

def details(request):
    return render(request, 'teaching/details.html')

def list(request):
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request, 'teaching/list.html', context)

def training(request, id_training=1):

    disciplines = []

    # Select the incoming training
    training = Training.objects.get(id=id_training)

    # Select the disciplines of the incoming training
    for id_mat in training.matieres:
        discipline = Discipline.objects.get(id=id_mat)
        disciplines.append(discipline)

    context['training'] = training
    context['disciplines'] = disciplines

    return render(request, 'teaching/training.html', context)
