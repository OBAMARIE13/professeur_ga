from django.db import models

# Create your models here.


class Banner(models.Model):
    image = models.FileField(upload_to="image_site")
    profession = models.CharField(max_length=255)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.nom
    
    
class About(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()        
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.titre
    
    
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
