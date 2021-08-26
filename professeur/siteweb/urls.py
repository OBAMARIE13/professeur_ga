from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index , name='index'),
    path('login/', views.login, name='login'),
    path('inscription/', views.inscription, name='inscription'),
    path('works/', views.works, name='works'),
    path('work/', views.work, name='work'),
]