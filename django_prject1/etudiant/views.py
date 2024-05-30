from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def etudiant(request):
    return render(request, 'etudiant.html')

def candidature(request):
    return render(request, 'candidature.html')

def suivis(request):
    return render(request, 'suivis.html')

