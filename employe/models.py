from django.db import models

class Employe(models.Model):
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    fonction = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    class Meta:
        db_table = "employe"