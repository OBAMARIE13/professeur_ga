from django.db import models


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





class Liens_sociaux(models.Model):
    icone = models.CharField(max_length=200)
    lien = models.TextField()
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Liens_sociaux'
        verbose_name_plural = 'Liens_sociaux'

    def __str__(self):
        return self.icone


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class Banner_skill(models.Model):
    image = models.FileField(upload_to="image_website")
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image


class Banner_course(models.Model):
    image = models.FileField(upload_to="image_website")
    description_image = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description_image

class Siteweb(models.Model):
	nom = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	email = models.EmailField()
	adresse = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Siteweb'
		verbose_name_plural = 'Sitewebs'
