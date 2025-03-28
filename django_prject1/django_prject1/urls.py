from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from etudiant import views
from etudiant.views import (
 sing_in, sing_up, log_out,
 forgot_password
)
from agent.views import (
 dashboard,status, info , univ ,home_agent
)

urlpatterns = [
 path('', views.home, name='home'),
 path('admin/', admin.site.urls),
 path('home/', views.home, name='home'),
 path('etudiant/', views.etudiant, name='etudiant'),
 path('candidature/', views.candidature, name='candidature'),
 path('suivis/', views.suivis, name="suivis"),
 path('', include('account.urls')),
 path('login', sing_in, name='sing_in'),
 path('register', sing_up, name='sing_up'),
 path('logout', log_out, name='log_out'),
 path('forgot-password', forgot_password, name='forgot_password'),
 path('dashboard',dashboard,name='dashboard'),
 path('status',status,name='status'),
 path('univ',univ,name='univ'),
 path('agent/', include('agent.urls')),
]




if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)