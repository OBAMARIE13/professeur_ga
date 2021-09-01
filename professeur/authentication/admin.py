from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):
    	list_display = ('civilite', 'name', 'prenom', 'email', 'profession', 'niveau_etude', 'password', 'verify_password', 'date_add', 'date_update', 'status')


@admin.register(models.Login)
class LoginAdmin(admin.ModelAdmin):
    	list_display = ('utilisateur', 'password', 'se_souvenir', 'password_forgot', 'date_add', 'date_update', 'status')
