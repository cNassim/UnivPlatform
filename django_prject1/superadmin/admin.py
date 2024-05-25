from django.contrib import admin
from .models import Agent, Spécialité, Pays, Etudiant, Université, Formation, Candidature

class AgentAdmin(admin.ModelAdmin):
    list_display = ('id_agent', 'Nom', 'Prenom', 'Email', 'Telephone')
    search_fields = ('Nom', 'Prenom', 'Email')

class SpécialitéAdmin(admin.ModelAdmin):
    list_display = ('id_spécialité', 'Nom', 'Responsable', 'Description')
    search_fields = ('Nom', 'Responsable')

class PaysAdmin(admin.ModelAdmin):
    list_display = ('id_pays', 'Nom', 'ville')
    search_fields = ('Nom', 'ville')


class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('id_etudiant', 'Nom', 'Prenom', 'Email', 'Date_de_naissance', 'Nationalité', 'CIN')
    search_fields = ('Nom', 'Prenom', 'Email', 'CIN')

class UniversitéAdmin(admin.ModelAdmin):
    list_display = ('id_univ', 'Nom', 'Email', 'Numero_de_telephone', 'FAX', 'adresse', 'id_pays')
    search_fields = ('Nom', 'Email')

class FormationAdmin(admin.ModelAdmin):
    list_display = ('id_formation', 'Nom', 'Description', 'Prérequis', 'Durée', 'Coût_de_formation', 'Langue', 'Programme', 'Campus', 'Niveau_d_étude', 'id_spécialité', 'id_univ')
    search_fields = ('Nom',)

class CandidatureAdmin(admin.ModelAdmin):
    list_display = ('id_candidature', 'Formation', 'Université', 'Spécialité', 'Status', 'Date_de_soumission', 'Lettre_de_motivation', 'id_agent', 'id_etudiant')
    search_fields = ('Formation', 'Université', 'Spécialité')


admin.site.register(Agent, AgentAdmin)
admin.site.register(Spécialité, SpécialitéAdmin)
admin.site.register(Pays, PaysAdmin)
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Université, UniversitéAdmin)
admin.site.register(Formation, FormationAdmin)
admin.site.register(Candidature, CandidatureAdmin)
