from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
	list_display = ('view_photo', 'profession_un', 'profession_deux', 'nom', 'citation', 'date_add', 'date_update', 'status')
	
 
	def view_photo(self, obj):
		return mark_safe(f'<img src="{obj.photo.url}" style="height:80px; width:130px">')
	view_photo.short_description = 'Apercu des images view_photo'
 

@admin.register(models.Gallerie)
class GallerieAdmin(admin.ModelAdmin):
	list_display = ('view_photo', 'nom', 'description', 'date_add', 'date_update', 'status')
	
 
	def view_photo(self, obj):
		return mark_safe(f'<img src="{obj.photo.url}" style="height:80px; width:130px">')
	view_photo.short_description = 'Apercu des images view_photo'


@admin.register(models.About_detail)
class About_detailAdmin(admin.ModelAdmin):
	list_display = ('titre_profession', 'description', 'date_add', 'date_update', 'status')


@admin.register(models.Liens_sociaux)
class Liens_sociauxAdmin(admin.ModelAdmin):
	list_display = ('icone', 'nom', 'lien', 'date_add', 'date_update', 'status')

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('nom', 'email', 'messages', 'date_add', 'date_update', 'status')

@admin.register(models.Banner_skill)
class Banner_skillAdmin(admin.ModelAdmin): 
    list_display = ('view_image', 'date_add', 'date_update', 'status')
    
    def view_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:80px; width:130px">')
    view_image.short_description = 'Apercu des images view_photo'


@admin.register(models.Banner_course)
class Banner_courseAdmin(admin.ModelAdmin): 
    list_display = ('view_image', 'description_image', 'date_add', 'date_update', 'status')
    
    def view_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:80px; width:130px">')
    view_image.short_description = 'Apercu des images view_photo'
