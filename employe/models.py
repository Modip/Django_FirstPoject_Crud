from django.db import models

class Person(models.Model):
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)

