from django.db import models

# Create your models here.

class Galleries(models.Model):
    titre = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.FileField(upload_to="image_professions")
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description
    
    
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name