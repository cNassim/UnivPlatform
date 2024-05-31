from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Candidature


def home(request):
    return render(request, 'home.html')

@login_required(login_url='sing_in')
def candidature(request):
    if request.method == 'POST':
        Nom = request.POST['Nom']
        Prenom = request.POST['Prenom']
        Email = request.POST['email']
        Lettre2motivation = request.POST['lettre_de_motivation']
        Date2naissance = request.POST['date_de_naissance']
        Nationalité = request.POST['nationalité']
        Cin = request.POST['CIN']
        
        # Get the currently logged-in user
        user = request.user

        # Create a new Candidature instance with the provided data and user information
        new_candidature = Candidature(
            id_etudiant=user.id,
            Nom=Nom,
            Prenom=Prenom,
            Email=Email,
            password=user.password,
            Date_de_naissance=Date2naissance,
            Nationalité=Nationalité,
            CIN=Cin,
            photo='test',
            id_agent = '2',
        )
        new_candidature.save()

    return render(request, 'candidature.html')

@login_required(login_url='sing_in')
def suivis(request):
    return render(request, 'suivis.html')

def sing_in(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.email, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('etudiant')
            else:
                return render(request, 'login.html', {'error': True, 'message': 'Mot de passe incorrect'})
        else:
            return render(request, 'login.html', {'error': True, 'message': "L'utilisateur n'existe pas"})

    return render(request, 'login.html', {})
def sing_up(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)

        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'register.html', {'error': True, 'message': 'Entrez un email valide s\'il vous plaît!'})

        if password != repassword:
            return render(request, 'register.html', {'error': True, 'message': 'Les deux mots de passe ne correspondent pas!'})

        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': True, 'message': f"Un utilisateur avec l'email {email} existe déjà!"})

        user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, username=email)
        
        
        login(request, user)
        return redirect('sing_in')

    return render(request, 'register.html', {})

@login_required(login_url='sing_in')
def etudiant(request):
    return render(request, 'etudiant.html', {})

def log_out(request):
    logout(request)
    return redirect('sing_in')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            # Handle email sending securely
            return render(request, "forgot_password.html", {'success': True, 'message': 'Un email de récupération a été envoyé.'})
        else:
            return render(request, "forgot_password.html", {'error': True, 'message': 'Cet utilisateur n\'existe pas.'})
    return render(request, "forgot_password.html", {})
