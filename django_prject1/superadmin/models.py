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
    photo = models.ImageField(upload_to='univers_photos/', null=True, blank=True)
    siteweb = models.URLField(max_length=200, null=True, blank=True)

    def _str_(self):
        return self.Nom

class Formation(models.Model):
    id_formation = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    id_université = models.IntegerField()

    def _str_(self):
        return self.Nom

class Candidature(models.Model):
    id_candidature = models.AutoField(primary_key=True)
    id_etudiant = models.IntegerField()
    photo = models.ImageField(upload_to='pic/', null=True, blank=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    Date_de_naissance = models.DateField()
    Nationalité = models.CharField(max_length=50)
    CIN = models.CharField(max_length=50)
    Date_de_soumission = models.DateTimeField()
    Lettre_de_motivation = models.CharField(max_length=50)
    BAC = models.ImageField(upload_to='doc/', null=True, blank=True)
    note_BAC = models.ImageField(upload_to='doc/', null=True, blank=True)
    universite1 = models.CharField(max_length=250)
    universite2 = models.CharField(max_length=250)
    formation2 = models.CharField(max_length=250)
    universite3 = models.CharField(max_length=250)
    universite4 = models.CharField(max_length=250)
    formation4 = models.CharField(max_length=250)
    universite5 = models.CharField(max_length=250)
    universite6 = models.CharField(max_length=250)
    universite7 = models.CharField(max_length=250)
    formation7 = models.CharField(max_length=200)
    universite8 = models.CharField(max_length=200)
    formation8 = models.CharField(max_length=200)
    status1 = models.CharField(max_length=50, null=True, blank=True)
    status2 = models.CharField(max_length=50, null=True, blank=True)
    status3 = models.CharField(max_length=50, null=True, blank=True)
    status4 = models.CharField(max_length=50, null=True, blank=True)
    status5 = models.CharField(max_length=50, null=True, blank=True)
    status6 = models.CharField(max_length=50, null=True, blank=True)
    status7 = models.CharField(max_length=50, null=True, blank=True)
    status8 = models.CharField(max_length=50, null=True, blank=True)
    id_agent = models.IntegerField()
    def _str_(self):
        return f"Candidature {self.id_candidature}"