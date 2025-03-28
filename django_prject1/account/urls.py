from django.contrib import admin
from django.urls import path, include

from account.views import (
    sing_in, sing_up, log_out,
)
urlpatterns = [
    path('login', sing_in, name='sing_in'),
    path('register', sing_up, name='sing_up'),
    path('logout', log_out, name='log_out'),
]
