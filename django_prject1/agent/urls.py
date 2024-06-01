from django.urls import path
from . import views

urlpatterns = [
 path('home/', views.home_agent, name='home_agent'), 
 path('info/', views.info, name='info'),
 path('student-info/', views.student_list, name='student-list'),  # List of students for the agent
 path('student-info/<int:student_id>/', views.student_detail, name='student-detail'),
 path('univ/', views.targeted_universities, name='targeted-universities'),  # Targeted universities view

]