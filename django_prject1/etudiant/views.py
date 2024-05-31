from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
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

        # Create a new Etudiant instance with the provided data and user information
        new_candidature = Candidature(
            id_etudiant=user.id,
            Nom=Nom,
            Prenom=Prenom,
            Email=Email,
            password=user.password,
            Date_de_naissance=Date2naissance,
            Nationalité=Nationalité,
            CIN=Cin,
            id_pays_id="1",
            photo='test'
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
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('etudiant')
            else:
                print("mot de pass incorrecte")
        else:
            print("User does not exist")

    return render(request, 'login.html', {})

def sing_up(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False:
            if password != repassword:
                error = True
                message = "Les deux mot de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"
        
        # register
        if error == False:
            user = User(
                username = name,
                email = email,
            )
            user.save()

            user.password = password
            user.set_password(user.password)
            user.save()

            return redirect('sing_in')


    context = {
        'error':error,
        'message':message
    }
    return render(request, 'register.html', context)


@login_required(login_url='sing_in')
def etudiant(request):
    return render(request, 'etudiant.html', {})

def log_out(request):
    logout(request)
    return redirect('sing_in')


def forgot_password(request):
    error = False
    success = False
    message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            print("processing forgot password")
            html = """
                <p> Hello, merci de cliquer pour modifier votre email </p>
            """

            msg = EmailMessage(
                "Modification de mot de pass!",
                html,
                "soroib0879@gmail.com",
                ["soro4827@gmail.com"],
            )

            msg.content_subtype = 'html'
            msg.send()
            message = "processing forgot password"
            success = True
        else:
            print("user does not exist")
            error = True
            message = "user does not exist"
    context = {
        'success': success,
        'error':error,
        'message':message
    }
    return render(request, "forgot_password.html", context)


def update_password(request):
    return render(request, "update_password.html", {})
