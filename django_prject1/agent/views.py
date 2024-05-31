from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'home_agent.html')
def status(request):
    return render(request, 'status.html')
def info(request):
    return render(request, 'student-info.html')
def univ(request):
    return render(request, 'universities.html')
