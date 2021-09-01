from django.db import models
from tinymce.models import HTMLField

TYPES_SKILLS = [
    ('A', 'Activités'),
    ('C', 'Compétences'),
]


# Create your models here.
class Biography(models.Model):
    photo = models.FileField(upload_to='image_curriculum')
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
    titre = models.CharField(max_length=255)
    abstract = models.TextField()
    auteurs = models.CharField(max_length=255)
    lien = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'

    def __str__(self):
        return self.auteurs


class About(models.Model):
    icone = models.TextField()
    profession = models.CharField(max_length=200)
    description = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.profession


class About_details(models.Model):
    profession = models.CharField(max_length=200)
    description_profession = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'About_details'
        verbose_name_plural = 'About_details'

    def __str__(self):
        return self.profession


# class About_details(models.Model):
#     profession = models.CharField(max_length = 200)
#     description_profession = models.TextField()

#     date_add = models.DateTimeField(auto_now_add=True)
#     date_update = models.DateTimeField(auto_now=True)
#     status = models.BooleanField(default=True)


#     class Meta():
#         verbose_name = 'About_details'
#         verbose_name_plural = 'About_details'

#     def __str__(self):
#         return self.profession


class Cv_header(models.Model):
    photo = models.FileField(upload_to='image_curriculum')
    nom = models.CharField(max_length=255)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Cv_header'
        verbose_name_plural = 'Cv_headers'

    def __str__(self):
        return self.nom


# This model describes user skills
class Background(models.Model):
    titre = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()
    description = HTMLField()
    type = models.CharField(max_length=1, choices=TYPES_SKILLS)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Background'
        verbose_name_plural = 'Backgrounds'

    def __str__(self):
        return self.titre
