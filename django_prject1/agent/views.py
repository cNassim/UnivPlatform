from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from etudiant.models import Candidature
from superadmin.models import Agent
from django.shortcuts import render, get_object_or_404
# Create your views here.
@login_required
def dashboard(request):
    agents = Agent.objects.all()
    return render(request, 'home_agent.html',{'agents' : agents})
@login_required
def status(request):
    user = request.user
    agent = Agent.objects.get(Email=request.user.email)
    candidatures = Candidature.objects.filter(id_agent=agent.id_agent)

    if request.method == "POST":
        for candidature in candidatures:
            universities_and_formations = candidature.get_universities_and_formations()
            for data in universities_and_formations:
                status_key = f'status_{candidature.id_candidature}_{data["universite"]}'
                new_status = request.POST.get(f"status_{candidature.id_candidature}_{data['universite']}")
                if new_status and new_status != data['status']:
                    # Update the status in the candidature object
                    for i in range(1, 9):
                        if getattr(candidature, f'universite{i}') == data['universite']:
                            setattr(candidature, f'status{i}', new_status)
                            candidature.save()
                            break
        return redirect('status')  # Redirect to the same page after updating

    return render(request, 'status.html', {'agent': agent, 'candidatures': candidatures})
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