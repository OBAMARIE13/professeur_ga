from django.urls import include, path
from . import views

app_name='curriculum'
urlpatterns = [
    path('', views.index, name='index'),
    path('skills/', views.skills, name='skills'),
    path('works/', views.works, name='works'),
]