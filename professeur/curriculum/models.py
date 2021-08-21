from django.db import models

# Create your models here.
class Biography(models.Model):
    photo = models.FileField(upload_to='image_biography')
    nom = models.CharField(max_length=200)
    titre = models.CharField(max_length=200)
    presentation = models.CharField(max_length=255) 
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = 'Biography'
        verbose_name_plural = 'Biographies'

    def __str__(self):
        return self.nom
    
    
    
class Research(models.Model):
    domaine = models.CharField(max_length=43)
    competence = models.CharField(max_length=200) 
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = 'Research'
        verbose_name_plural = 'Researches'

    def __str__(self):
        return self.domaine
    
    
class Publication(models.Model):
    titre = models.CharField(max_length=43)
    competence = models.CharField(max_length=200) 
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = 'Research'
        verbose_name_plural = 'Researches'

    def __str__(self):
        return self.domaine