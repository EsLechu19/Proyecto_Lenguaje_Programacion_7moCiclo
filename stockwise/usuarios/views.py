from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'usuarios/login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })

    return render(request, 'usuarios/login.html')


def logout_usuario(request):
    logout(request)
    return redirect('login')