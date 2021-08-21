from django.urls import include, path
from . import views

app_name='authentication'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
]