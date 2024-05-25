from django.db import models 

class Agent(models.Model):
    id_agent = models.IntegerField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    Telephone = models.IntegerField()

class Spécialité(models.Model):
    id_spécialité = models.IntegerField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Responsable = models.CharField(max_length=50, blank=True, null=True)
    Description = models.CharField(max_length=50, blank=True, null=True)

class Pays(models.Model):
    id_pays = models.IntegerField(primary_key=True)
    Nom = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)

class Etudiant(models.Model):
    id_etudiant = models.IntegerField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    Date_de_naissance = models.CharField(max_length=50)
    Nationalité = models.CharField(max_length=50)
    CIN = models.CharField(max_length=50)
    id_pays = models.ForeignKey(Pays, on_delete=models.CASCADE)

class Université(models.Model):
    id_univ = models.IntegerField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Numero_de_telephone = models.CharField(max_length=50)
    FAX = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    id_pays = models.ForeignKey(Pays, on_delete=models.CASCADE)

class Formation(models.Model):
    id_formation = models.IntegerField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Prérequis = models.CharField(max_length=50)
    Durée = models.TimeField()
    Coût_de_formation = models.FloatField()
    Langue = models.CharField(max_length=50)
    Programme = models.CharField(max_length=50)
    Campus = models.CharField(max_length=50)
    Niveau_d_étude = models.CharField(max_length=50)
    id_spécialité = models.ForeignKey(Spécialité, on_delete=models.CASCADE)
    id_univ = models.ForeignKey(Université, on_delete=models.CASCADE)

class Candidature(models.Model):
    id_candidature = models.CharField(max_length=50, primary_key=True)
    Formation = models.CharField(max_length=50)
    Université = models.CharField(max_length=50)
    Spécialité = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)
    Date_de_soumission = models.DateTimeField()
    Lettre_de_motivation = models.CharField(max_length=50)
    id_agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

