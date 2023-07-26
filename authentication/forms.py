from django.db import models
from django import forms

# le widget determine la facon dont on affiche le champs
class LoginForm(forms.Form):
    username  = forms.CharField(label="Nom d'utilisateur",max_length=30)
    password = forms.CharField(widget=forms.PasswordInput,label="Mot de passse ",max_length=30)