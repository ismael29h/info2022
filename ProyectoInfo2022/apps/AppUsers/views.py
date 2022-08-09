from django.shortcuts import render, redirect

# Create your views here.

from django.contrib import messages
from django.contrib.auth.models import User, auth

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Contraseña inválida.')
            return redirect('/login.html')

    else:
        return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')