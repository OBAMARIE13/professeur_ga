from django import forms

class Registration(forms.Form): 
    civilite = forms.CharField(max_length=255)
    name = forms.CharField(max_length=100)
    prenom = forms.CharField(max_length=100)
    email = forms.EmailField()
    profession = forms.CharField(max_length=200)
    niveau_etude = forms.CharField(max_length=100)
    password = forms.CharField(max_length=255)
    verify_password = forms.CharField(max_length=255)
    date_add = forms.DateTimeField(auto_now_add=True)
    date_update = forms.DateTimeField(auto_now=True)
    status = forms.BooleanField(default=True)