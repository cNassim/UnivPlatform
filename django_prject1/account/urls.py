from django.contrib import admin
from django.urls import path, include

from account.views import (
    sing_in, sing_up, log_out,
    forgot_password, update_password
)
urlpatterns = [
    path('login', sing_in, name='sing_in'),
    path('register', sing_up, name='sing_up'),
    path('logout', log_out, name='log_out'),
    path('forgot-password', forgot_password, name='forgot_password'),
    path('update-password', update_password, name='update_password'),
]
