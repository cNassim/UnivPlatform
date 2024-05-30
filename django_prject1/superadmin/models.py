from django.db import models


class Agent(models.Model):
    id_agent = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    Telephone = models.CharField(max_length=15, default='0000000000')
    photo = models.ImageField(upload_to='agent_photos/', null=True, blank=True)

class Spécialité(models.Model):
    id_spécialité = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Description = models.CharField(max_length=100, blank=True, null=True)

class Pays(models.Model):
    id_pays = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)

    def __str__(self):
        return self.Nom

class Etudiant(models.Model):
    id_etudiant = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    Date_de_naissance = models.DateField()
    Nationalité = models.CharField(max_length=50)
    CIN = models.CharField(max_length=50)
    id_pays = models.ForeignKey(Pays, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='etudiant_photos/', null=True, blank=True)

class Université(models.Model):
    id_univ = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Numero_de_telephone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    id_pays = models.ForeignKey(Pays, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='univers_photos/', null=True, blank=True)


    def __str__(self):
        return self.Nom

class Formation(models.Model):
    id_formation = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Prérequis = models.CharField(max_length=50)
    Durée = models.DurationField()
    Coût_de_formation = models.DecimalField(max_digits=10, decimal_places=2)
    Langue = models.CharField(max_length=50)
    Programme = models.CharField(max_length=50)
    Campus = models.CharField(max_length=50)
    Niveau_d_étude = models.CharField(max_length=50)
    id_spécialité = models.ForeignKey(Spécialité, on_delete=models.CASCADE)
    id_univ = models.ForeignKey(Université, on_delete=models.CASCADE)

class Candidature(models.Model):
    id_candidature = models.AutoField(primary_key=True)
    Date_de_soumission = models.DateTimeField()
    Lettre_de_motivation = models.CharField(max_length=50)
    id_agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    universite1 = models.CharField(max_length=50)
    formation1 = models.CharField(max_length=50)
    universite2 = models.CharField(max_length=50)
    formation2 = models.CharField(max_length=50)
    universite3 = models.CharField(max_length=50)
    formation3 = models.CharField(max_length=50)
    universite4 = models.CharField(max_length=50)
    formation4 = models.CharField(max_length=50)
    universite5 = models.CharField(max_length=50)
    formation5 = models.CharField(max_length=50)
    universite6 = models.CharField(max_length=50)
    formation6 = models.CharField(max_length=50)
    universite7 = models.CharField(max_length=50)
    formation7 = models.CharField(max_length=50)
    universite8 = models.CharField(max_length=50)
    formation8 = models.CharField(max_length=50)
    status1 = models.CharField(max_length=50)
    status2 = models.CharField(max_length=50)
    status3 = models.CharField(max_length=50)
    status4 = models.CharField(max_length=50)
    status5 = models.CharField(max_length=50)
    status6 = models.CharField(max_length=50)
    status7 = models.CharField(max_length=50)
    status8 = models.CharField(max_length=50)

    def __str__(self):
        return f"Candidature {self.id_candidature}"
