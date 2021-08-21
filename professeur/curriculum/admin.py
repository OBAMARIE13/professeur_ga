from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(models.Biography)
class BiographyAdmin(admin.ModelAdmin):
	list_display = ('view_photo', 'nom', 'titre', 'presentation', 'date_add', 'date_update', 'status')
	
 
	def view_photo(self, obj):
		return mark_safe(f'<img src="{obj.photo.url}" style="height:80px; width:130px">')
	view_photo.short_description = 'Apercu des images view_photo'



@admin.register(models.Research)
class ResearchAdmin(admin.ModelAdmin):
	list_display = ('domaine', 'competence', 'date_add', 'date_update', 'status')
 
 

@admin.register(models.Publication)
class PublicationAdmin(admin.ModelAdmin):
    	list_display = ('titre', 'abstract', 'auteurs', 'date_add', 'date_update', 'status')


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    	list_display = ('icone', 'profession', 'description', 'date_add', 'date_update', 'status')


@admin.register(models.About_details)
class About_detailsAdmin(admin.ModelAdmin):
    	list_display = ('profession', 'description_profession', 'date_add', 'date_update', 'status')

@admin.register(models.Cv_header)
class Cv_headerAdmin(admin.ModelAdmin):
    	list_display = ('photo', 'nom', 'date_add', 'date_update', 'status')


@admin.register(models.Background)
class BackgroundAdmin(admin.ModelAdmin):
    	list_display = ('titre', 'description', 'date_add', 'date_update', 'status')
