from django.shortcuts import render, redirect

# Create your views here.

from django.contrib import messages
from django.contrib.auth.models import User, auth

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'El nombre de usuario está en uso.')
                return redirect('/registro.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'El correo electrónico ya está registrado.')
                return redirect('/registro.html')
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email)
                user.save()
                
                return redirect('/login.html')


        else:
            messages.info(request, 'Las contraseñas no coinciden.')
            return redirect('/registro.html')
            
    else:
        return render(request, 'usuarios/register.html')


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