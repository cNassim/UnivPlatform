from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Candidature
from superadmin.models import Université,Formation


def home(request):
    return render(request, 'home.html')

@login_required(login_url='sing_in')
def candidature(request):

    candidatures = Candidature.objects.all()
    user_candidatures = candidatures.filter(id_etudiant=request.user.id)
    Universités = Université.objects.all()
    Formations = Formation.objects.all()
    if request.method == 'POST':
        Nom = request.POST['Nom']
        Prenom = request.POST['Prenom']
        Email = request.POST['email']
        Lettre2motivation = request.POST['lettre_de_motivation']
        Date2naissance = request.POST['date_de_naissance']
        Nationalité = request.POST['nationalité']
        Cin = request.POST['CIN']
        bac= request.FILES['Baclo']
        bultinbac= request.FILES['Bulletin_BAC']
        pic = request.FILES['photo']
        un1=request.POST['u1']
        fo1=request.POST['s1']
        un2=request.POST['u2']
        fo2=request.POST['s2']
        un3=request.POST['u3']
        fo3=request.POST['s3']
        un4=request.POST['u4']
        fo4=request.POST['s4']
        un5=request.POST['u5']
        fo5=request.POST['s5']
        un6=request.POST['u6']
        fo6=request.POST['s6']
        un7=request.POST['u7']
        fo7=request.POST['s7']
        un8=request.POST['u8']
        fo8=request.POST['s8']
        # Get the currently logged-in user
        user = request.user

        # Create a new Candidature instance with the provided data and user information
        new_candidature = Candidature(
            id_etudiant=user.id,
            Nom=Nom,
            Prenom=Prenom,
            Email=Email,
            password=user.password,
            Lettre_de_motivation = Lettre2motivation,
            Date_de_naissance=Date2naissance,
            Nationalité=Nationalité,
            CIN=Cin,
            BAC = bac,
            note_BAC = bultinbac,
            photo=pic,
            id_agent = '2',
            universite1=un1,
            formation1=fo1,
            universite2=un2,
            formation2=fo2,
            universite3=un3,
            formation3=fo3,
            universite4=un4,
            formation4=fo4,
            universite5=un5,
            formation5=fo5,
            universite6=un6,
            formation6=fo6,
            universite7=un7,
            formation7=fo7,
            universite8=un8,
            formation8=fo8
        )
        new_candidature.save()

    return render(request, 'candidature.html',{'user_candidatures': user_candidatures,'Universités': Universités, 'Formations': Formations})

@login_required(login_url='sing_in')
def suivis(request):
    candidatures = Candidature.objects.all()
    return render(request, 'suivis.html',{'candidatures' : candidatures})

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
