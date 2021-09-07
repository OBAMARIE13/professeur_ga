from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authentication/', include('authentication.urls')),
    path('curriculum/', include('curriculum.urls')),
    path('teaching/', include('teaching.urls')),
    path('checkup', views.checkup, name='checkup')
    
]
