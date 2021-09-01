from django.shortcuts import render
from . import models

def index(request):
    banner = models.Banner.objects.filter(status=True).first
    return render(request, 'index.html', locals())

