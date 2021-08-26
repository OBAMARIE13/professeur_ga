from django.core.checks import messages
from django.db import models

# Create your models here.


class Banner(models.Model):
    photo = models.FileField(upload_to='website_image')
    profession_un = models.CharField(max_length=255)
    profession_deux = models.CharField(max_length=255)
    nom = models.CharField(max_length=200)
    citation = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    class Meta():
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    
    def __str__(self):
        return self.nom
    
    
class Gallerie(models.Model):
    photo = models.FileField(upload_to='website_image')
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=200)       
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    class Meta():
        verbose_name = 'Gallerie'
        verbose_name_plural = 'Galleries'
    
    def __str__(self):
        return self.nom
    
  
class Liens_sociaux(models.Model):
    icone = models.TextField(null=True, blank=True)
    nom = models.CharField(max_length=200)
    lien = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta():
        verbose_name = 'Liens_sociaux'
        verbose_name_plural = 'Liens_sociaux'
    
    def __str__(self):
        return self.nom
    

class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta():
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return self.nom


class Banner_skills(models.Model):
    image = models.FileField(upload_to='website_image')
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    class Meta():
        verbose_name = 'Banner_skills'
        verbose_name_plural = 'Banner_skills'
    
    def __str__(self):
        return self.image 
    
class Banner_coursses(models.Model):
    image = models.FileField(upload_to='website_image')
    description_image = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    class Meta():
        verbose_name = 'Banner_coursses'
        verbose_name_plural = 'Banner_coursses'
    
    def __str__(self):
        return self.description_image 