from django.db import models

# Create your models here.

class employeur(models.Model):
    nom = models.CharField(max_length=30)
    email = models.CharField(max_length=30)