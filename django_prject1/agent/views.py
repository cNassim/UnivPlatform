from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from etudiant.models import Candidature
from superadmin.models import Agent
from django.shortcuts import render, get_object_or_404
# Create your views here.
def dashboard(request):
    agents = Agent.objects.all()
    return render(request, 'home_agent.html',{'agents' : agents})
def status(request):
    user = request.user
    agent = Agent.objects.get(Email=request.user.email)
    candidatures = Candidature.objects.filter(id_agent=agent.id_agent)
    return render(request, 'status.html',{'agent': agent, 'candidatures': candidatures})
@login_required
def info(request):
    user = request.user
    # Récupérer l'agent connecté
    agent = Agent.objects.get(Email=request.user.email)
    # Filtrer les candidatures liées à cet agent
    candidatures = Candidature.objects.filter(id_agent=agent.id_agent)
    return render(request, 'student-info.html',{'agent': agent, 'candidatures': candidatures})
def univ(request):
    return render(request, 'universities.html')
@login_required
def home_agent(request):
    return render(request, 'home_agent.html')
@login_required
def student_list(request):
    return render(request, 'student-info.html')
@login_required
def student_detail(request):
    return render(request, 'student_detail.html')