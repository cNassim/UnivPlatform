from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Agent , Student
from django.shortcuts import render, get_object_or_404
# Create your views here.
def dashboard(request):
 return render(request, 'home_agent.html')
def status(request):
 return render(request, 'status.html')
def info(request):
 return render(request, 'student-info.html')
def univ(request):
 return render(request, 'universities.html')


@login_required
def home_agent(request):
 # Retrieve the agent corresponding to the logged-in user
 agent = Agent.objects.get(email=request.user.email)
 return render(request, 'home_agent.html', {'agent': agent})
def info(request):
 # Your logic to retrieve information about the student or agent
 return render(request, 'student-info.html') 
#==================================
@login_required
def student_list(request):
    agent = get_object_or_404(Agent, user=request.user)  # Assume agent is related to the logged-in user
    students = Student.objects.filter(agent=agent)
    context = {
        'students': students,
        'agent': agent,
    }
    return render(request, 'student-info.html', context)

@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'student_detail.html', context)
#=======================================
@login_required
def targeted_universities(request):
    agent = get_object_or_404(Agent, user=request.user)
    students = Student.objects.filter(agent=agent)
    selected_student_id = request.GET.get('student')
    selected_student = None
    universities = None

    if selected_student_id:
        selected_student = get_object_or_404(Student, id=selected_student_id)
        universities = selected_student.universities.all()[:8]  # Assuming a many-to-many relationship

    context = {
        'students': students,
        'selected_student': selected_student,
        'universities': universities,
    }
    return render(request, 'universities.html', context)