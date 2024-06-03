from django.db import models

class Candidature(models.Model):
    id_candidature = models.AutoField(primary_key=True)
    id_etudiant = models.IntegerField()
    photo = models.ImageField(upload_to='media/', null=True, blank=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    password = models.CharField(max_length=500)
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
    formation5= models.CharField(max_length=250, null=True, blank=True)
    universite6 = models.CharField(max_length=250, null=True, blank=True)
    formation6 = models.CharField(max_length=250, null=True, blank=True)
    universite7 = models.CharField(max_length=250, null=True, blank=True)
    formation7 = models.CharField(max_length=250, null=True, blank=True)
    universite8 = models.CharField(max_length=250, null=True, blank=True)
    formation8 = models.CharField(max_length=250, null=True, blank=True)
    status1 = models.CharField(max_length=50, default='pending')
    status2 = models.CharField(max_length=50, default='pending')
    status3 = models.CharField(max_length=50, default='pending')
    status4 = models.CharField(max_length=50, default='pending')
    status5 = models.CharField(max_length=50, default='pending')
    status6 = models.CharField(max_length=50, default='pending')
    status7 = models.CharField(max_length=50, default='pending')
    status8 = models.CharField(max_length=50, default='pending')
    id_agent = models.IntegerField()
    def get_universities_and_formations(self):
        data = []
        for i in range(1, 9):
            universite = getattr(self, f'universite{i}', None)
            formation = getattr(self, f'formation{i}', None)
            status = getattr(self, f'status{i}', None)
            if universite and formation:
                data.append({
                    'universite': universite,
                    'formation': formation,
                    'status': status
                })
        return data
    def _str_(self):
        return f"Candidature {self.id_candidature}"