from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from etudiant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('etudiant/', views.etudiant, name='etudiant'),
    path('candidature/', views.candidature, name='candidature'),
    path('suivis/',views.suivis,name="suivis"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
