
from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from django.utils.html import format_html
from .models import Agent, Spécialité, Pays, Etudiant, Université, Formation, Candidature

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id_agent', 'Nom', 'Prenom', 'Email', 'Telephone', 'display_photo')
    search_fields = ('Nom', 'Prenom', 'Email')
    list_filter = ('Nom',)
    ordering = ('Nom',)
    readonly_fields = ('id_agent',)
    fieldsets = (
        (None, {
            'fields': ('Nom', 'Prenom', 'Email', 'Telephone', 'photo')
        }),
        ('Security', {
            'fields': ('password',)
        }),
    )

    def display_photo(self, obj):
        return format_html('<img src="{}" width="50" height="50"/>', obj.photo.url) if obj.photo else None
    display_photo.short_description = 'Photo'


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('id_etudiant', 'Nom', 'Prenom', 'Email', 'Date_de_naissance', 'Nationalité', 'CIN', 'display_photo')
    search_fields = ('Nom', 'Prenom', 'Email', 'CIN')
    list_filter = ('Nom', 'Nationalité')
    ordering = ('Nom',)
    readonly_fields = ('id_etudiant',)
    fieldsets = (
        (None, {
            'fields': ('Nom', 'Prenom', 'Email', 'Date_de_naissance', 'Nationalité', 'CIN', 'photo')
        }),
        ('Security', {
            'fields': ('password',)
        }),
        ('Location', {
            'fields': ('id_pays',)
        }),
    )

    def display_photo(self, obj):
        return format_html('<img src="{}" width="50" height="50"/>', obj.photo.url) if obj.photo else None
    display_photo.short_description = 'Photo'

@admin.register(Université)
class UniversitéAdmin(admin.ModelAdmin):
    list_display = ('id_univ', 'Nom', 'Email', 'Numero_de_telephone', 'adresse', 'id_pays', 'display_photo')
    search_fields = ('Nom', 'Email', 'Numero_de_telephone', 'adresse',)
    list_filter = ('Nom',)
    ordering = ('Nom',)
    readonly_fields = ('id_univ',)

    fieldsets = (
        (None, {
            'fields': ('Nom', 'Email', 'Numero_de_telephone', 'adresse', 'id_pays', 'photo')
        }),
    )

    def display_photo(self, obj):
        return format_html('<img src="{}" width="150"/>', obj.photo.url) if obj.photo else None
    display_photo.short_description = 'Photo'

    def list_edited_image(self, obj):
        if obj.photo:
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" width="100"/></a>',
                obj.photo.url,
                obj.photo.url
            )
        else:
            return 'No Photo'
    list_edited_image.short_description = 'Image Modifiée'

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('id_formation', 'Nom', 'Description', 'Prérequis', 'Durée', 'Coût_de_formation', 'Langue', 'Programme', 'Campus', 'Niveau_d_étude', 'id_spécialité', 'id_univ')
    search_fields = ('Nom', 'Description', 'Prérequis', 'Langue', 'Programme', 'Campus', 'Niveau_d_étude')
    list_filter = ('Nom', 'Langue', 'Niveau_d_étude')
    ordering = ('Nom',)
    readonly_fields = ('id_formation',)
    fieldsets = (
        (None, {
            'fields': ('Nom', 'Description', 'Prérequis', 'Durée', 'Coût_de_formation', 'Langue', 'Programme', 'Campus', 'Niveau_d_étude', 'id_spécialité', 'id_univ')
        }),
    )

@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ('id_candidature', 'Date_de_soumission', 'Lettre_de_motivation', 'id_agent', 'id_etudiant', 'universite1', 'formation1', 'universite2', 'formation2', 'universite3', 'formation3', 'universite4', 'formation4', 'universite5', 'formation5', 'universite6', 'formation6', 'universite7', 'formation7', 'universite8', 'formation8', 'status1', 'status2', 'status3', 'status4', 'status5', 'status6', 'status7', 'status8')
    search_fields = ('id_candidature', 'Date_de_soumission', 'Lettre_de_motivation', 'universite1', 'formation1', 'universite2', 'formation2', 'universite3', 'formation3', 'universite4', 'formation4', 'universite5', 'formation5', 'universite6', 'formation6', 'universite7', 'formation7', 'universite8', 'formation8')
    list_filter = ('Date_de_soumission', 'status1', 'status2', 'status3', 'status4', 'status5', 'status6', 'status7', 'status8')
    ordering = ('-Date_de_soumission',)
    readonly_fields = ('id_candidature',)
    fieldsets = (
        (None, {
            'fields': ('Date_de_soumission', 'Lettre_de_motivation', 'id_agent', 'id_etudiant')
        }),
        ('Preferences', {
            'fields': ('universite1', 'formation1', 'status1', 'universite2', 'formation2', 'status2', 'universite3', 'formation3', 'status3', 'universite4', 'formation4', 'status4', 'universite5', 'formation5', 'status5', 'universite6', 'formation6', 'status6', 'universite7', 'formation7', 'status7', 'universite8', 'formation8', 'status8')
        }),
    )
@admin.register(Spécialité)
class SpécialitéAdmin(admin.ModelAdmin):
    list_display = ('id_spécialité', 'Nom', 'Description')
    search_fields = ['Nom', 'Description']  
    ordering = ('Nom',)
    readonly_fields = ('id_spécialité',)

@admin.register(Pays)
class PaysAdmin(admin.ModelAdmin):
    list_display = ('id_pays', 'Nom', 'ville')
    search_fields = ('Nom', 'ville')
    list_filter = ('Nom',)
    ordering = ('Nom',)
    readonly_fields = ('id_pays',)
