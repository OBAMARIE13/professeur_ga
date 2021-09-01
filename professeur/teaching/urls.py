from django.urls import include, path
from . import views

app_name='teaching'
urlpatterns = [
    path('courses', views.courses, name='courses'),
    path('details/', views.details, name='details'),
    path('list/', views.list, name='list'),
    path('training/', views.training, name='training'),
]