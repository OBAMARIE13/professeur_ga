from django.db import models

# Create your models here.
class Registration(models.Model):
    
    civilite = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    profession = models.CharField(max_length=200)
    niveau_etude = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    verify_password = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = 'Registration'
        verbose_name_plural = 'Registrations'

    def __str__(self):
        return self.name
    
    

class Login(models.Model):
    utilisateur = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    se_souvenir = models.BooleanField(default=False)
    password_forgot = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = 'Login'
        verbose_name_plural = 'Logins'

    def __str__(self):
        return self.utilisateur