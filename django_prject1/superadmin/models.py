from django.db import models

class Agent(models.Model):
    id_agent = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    Telephone = models.CharField(max_length=15)

    def _str_(self):
        return f"{self.Nom} {self.Prenom}"

class Université(models.Model):
    id_univ = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Numero_de_telephone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    pays = models.CharField(max_length=200)
    siteweb = models.URLField(max_length=200, null=True, blank=True)

    def _str_(self):
        return self.Nom

class Formation(models.Model):
    id_formation = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)

    def _str_(self):
        return self.Nom