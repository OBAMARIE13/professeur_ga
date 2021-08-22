from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Galleries)
class GalleriesAdmin(admin.ModelAdmin):
    list_display = ["titre", "description", "image", "date_add", "date_update", "status"]
    
    

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "date_add", "date_update", "status"]