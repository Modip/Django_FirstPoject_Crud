from django.db import models

class Employeur(models.Model):
    nom = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    class Meta:
        db_table = "employeur"