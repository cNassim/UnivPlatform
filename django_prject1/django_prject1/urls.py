from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from etudiant import views
from etudiant.views import (
    sing_in, sing_up, log_out,
    forgot_password, update_password
)

urlpatterns = [
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
    path('update-password', update_password, name='update_password'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
