from django.core.checks import messages
from django.db import models

# Create your models here.


class Banner(models.Model):
    photo = models.FileField(upload_to="image_website")
    profession_un = models.CharField(max_length=255)
    profession_deux = models.CharField(max_length=255)
    nom = models.CharField(max_length=200)
    citation = models.TextField()
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.nom
    
    
class Gallerie(models.Model):
    photo = models.FileField(upload_to="image_website")
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=200)       
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.nom
    
    
class About_detail(models.Model):
    titre_profession = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.titre_profession
    
    
class Liens_sociaux(models.Model):
    icone = models.TextField
    nom = models.CharField(max_length=200)
    lien = models.TextField()
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
    

class Contacts(models.Model):
    nom = models.TextField
    email = models.CharField(max_length=200)
    messages = models.TextField()
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom


class Banner_skills(models.Model):
    image = models.FileField(upload_to="image_website")
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.image 
    
class Banner_coursses(models.Model):
    image = models.FileField(upload_to="image_website")
    description_image = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.description_image 