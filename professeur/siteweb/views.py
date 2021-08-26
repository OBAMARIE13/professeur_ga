from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    banner = models.Banner.objects.filter(status=True).first
    return render(request, 'index.html', locals())


def login(request):
    return render(request, "login.html")


def inscription(request):
    return render(request, "inscription.html")

def works(request):
    return render(request, 'works.html')

def work(request):
    return render(request, 'work.html')
    