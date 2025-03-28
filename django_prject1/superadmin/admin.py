from django.contrib import admin
from .models import Agent, Université, Formation
from etudiant.models import Candidature 

class AgentAdmin(admin.ModelAdmin):
    list_display = ('id_agent', 'Nom', 'Prenom', 'Email', 'Telephone')

class UniversitéAdmin(admin.ModelAdmin):
    list_display = ('id_univ', 'Nom', 'Email', 'Numero_de_telephone', 'adresse', 'pays', 'siteweb')

class FormationAdmin(admin.ModelAdmin):
    list_display = ('id_formation', 'Nom', 'Description')

class CandidatureAdmin(admin.ModelAdmin):
    list_display = ('id_candidature', 'Nom', 'Prenom', 'Email', 'Date_de_naissance', 'Nationalité', 'Date_de_soumission', 'status1', 'status2', 'status3', 'status4', 'status5', 'status6', 'status7', 'status8')
    list_filter = ('status1', 'status2', 'status3', 'status4', 'status5', 'status6', 'status7', 'status8')

admin.site.register(Agent, AgentAdmin)
admin.site.register(Université, UniversitéAdmin)
admin.site.register(Formation, FormationAdmin)
admin.site.register(Candidature, CandidatureAdmin)
