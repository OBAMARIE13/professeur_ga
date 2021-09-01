from django.db import models
from multiselectfield import MultiSelectField

STATUT = [
    ('C', 'En cours'),
    ('A', 'En attente'),
    ('T', 'Terminé'),
]


class Module(models.Model):
    nom = models.CharField(max_length=100)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):
        return self.nom


class Discipline(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.CharField(max_length=255)
    lien = models.URLField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Discipline'
        verbose_name_plural = 'Disciplines'

    def __str__(self):
        return self.titre


# Setting MATIERES with all the recorded disciplines
mats = Discipline.objects.all()
MATIERES = []
for mat in mats:
    MATIERES.append((mat.id, mat.titre))


class Training(models.Model):
    intitule = models.CharField(max_length=100, verbose_name='Intitulé')
    date_debut = models.DateField(verbose_name='Date de début')
    date_fin = models.DateField(verbose_name='Date de fin')
    mot_de_passe = models.CharField(max_length=255)
    matieres = MultiSelectField(choices=MATIERES, verbose_name='Matières')
    statut = models.CharField(max_length=1, choices=STATUT, verbose_name='Etat')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Formation'
        verbose_name_plural = 'Formations'

    def __str__(self):
        return self.intitule
