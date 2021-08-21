from django.shortcuts import render

def courses(request):
    return render(request, 'teaching/courses.html')

def details(request):
    return render(request, 'teaching/details.html')
