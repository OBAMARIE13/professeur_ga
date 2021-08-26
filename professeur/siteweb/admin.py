from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ["image", "profession", "nom", "description", "status", "date_add", "date_update"]
    
@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["titre", "description", "status", "date_add", "date_update"]
    
@admin.register(models.About_detail)
class About_detailAdmin(admin.ModelAdmin):
    list_display = ["titre_profession", "description", "status", "date_add", "date_update"]


@admin.register(models.Liens_sociaux)
class BannerAdmin(admin.ModelAdmin):
    list_display = ["icone", "nom", "lien", "status", "date_add", "date_update"]
