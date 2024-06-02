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

from django.db import models

class Candidature(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ]

    id_candidature = models.AutoField(primary_key=True)
    id_etudiant = models.IntegerField()
    photo = models.ImageField(upload_to='media/', null=True, blank=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    Date_de_naissance = models.DateField()
    Nationalité = models.CharField(max_length=50)
    CIN = models.CharField(max_length=50)
    Date_de_soumission = models.DateTimeField(auto_now_add=True)
    Lettre_de_motivation = models.CharField(max_length=50)
    BAC = models.ImageField(upload_to='media/', null=True, blank=True)
    note_BAC = models.ImageField(upload_to='media/', null=True, blank=True)
    universite1 = models.CharField(max_length=250, null=True, blank=True)
    formation1 = models.CharField(max_length=250, null=True, blank=True)
    universite2 = models.CharField(max_length=250, null=True, blank=True)
    formation2 = models.CharField(max_length=250, null=True, blank=True)
    universite3 = models.CharField(max_length=250, null=True, blank=True)
    formation3 = models.CharField(max_length=250, null=True, blank=True)
    universite4 = models.CharField(max_length=250, null=True, blank=True)
    formation4 = models.CharField(max_length=250, null=True, blank=True)
    universite5 = models.CharField(max_length=250, null=True, blank=True)
    formation5 = models.CharField(max_length=250, null=True, blank=True)
    universite6 = models.CharField(max_length=250, null=True, blank=True)
    formation6 = models.CharField(max_length=250, null=True, blank=True)
    universite7 = models.CharField(max_length=250, null=True, blank=True)
    formation7 = models.CharField(max_length=250, null=True, blank=True)
    universite8 = models.CharField(max_length=250, null=True, blank=True)
    formation8 = models.CharField(max_length=250, null=True, blank=True)
    status1 = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    status2 = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    status3 = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    status4 = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    status5 = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    status6 = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    status7 = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    status8 = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Candidature {self.id_candidature}"
