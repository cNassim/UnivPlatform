from django.db import models 

class Agent(models.Model):
    id_agent = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    Telephone = models.CharField(max_length=15)

class Spécialité(models.Model):
    id_spécialité = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Responsable = models.CharField(max_length=50, blank=True, null=True)
    Description = models.CharField(max_length=50, blank=True, null=True)

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


class Université(models.Model):
    id_univ = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Numero_de_telephone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='universite_photos/', null=True, blank=True)
    id_pays = models.ForeignKey(Pays, on_delete=models.CASCADE)

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
    Formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    Université = models.ForeignKey(Université, on_delete=models.CASCADE)
    Spécialité = models.ForeignKey(Spécialité, on_delete=models.CASCADE)
    Status = models.CharField(max_length=50)
    Date_de_soumission = models.DateTimeField()
    Lettre_de_motivation = models.CharField(max_length=50)
    id_agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
