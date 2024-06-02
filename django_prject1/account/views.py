from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Q
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from superadmin.models import Agent



def sing_in(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.email, password=password)
            if auth_user:
                login(request, auth_user)
                # Vérifier si l'utilisateur authentifié est un agent
                try:
                    agent = Agent.objects.get(Email=email)
                    return redirect('dashboard')
                except Agent.DoesNotExist:
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

