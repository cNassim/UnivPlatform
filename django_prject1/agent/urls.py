from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
 path('home/', views.home_agent, name='home_agent'), 
 path('info/', views.info, name='info'),
 path('student-info/', views.student_list, name='student-list'),  # List of students for the agent
 path('student-info/<int:student_id>/', views.student_detail, name='student-detail'),  # Targeted universities view

]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)