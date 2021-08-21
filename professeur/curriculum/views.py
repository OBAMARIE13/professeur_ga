from django.shortcuts import render

def index(request):
    return render(request, 'curriculum/index.html')

def skills(request):
    return render(request, 'curriculum/skills.html')

def works(request):
    return render(request, 'curriculum/works.html')
