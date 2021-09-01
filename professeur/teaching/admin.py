from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add', 'date_update', 'status')


@admin.register(models.Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('titre', 'image', 'description', 'lien', 'module', 'date_add', 'date_update', 'status')

    def image(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="height:80px; width:130px">')

    image.short_description = 'Image du cours'


@admin.register(models.Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('intitule', 'date_debut', 'date_fin', 'mot_de_passe', 'matieres', 'statut', 'date_add', 'date_update', 'status')