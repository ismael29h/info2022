from django.urls import path
from . import views


urlpatterns = [
    path('registro.html', views.registro, name='registro'),
    path('login.html', views.login, name='login'),
    path('logout.html', views.logout, name='logout'),
]