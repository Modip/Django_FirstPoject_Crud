from django.db import models

class Employe(models.Model):
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    fonction = models.CharField(max_length=30)
    class Meta:
        db_table = "employe"