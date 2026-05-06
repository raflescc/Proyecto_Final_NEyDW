from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

# Create your views here.


User = get_user_model()

# Registro
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Usuario ya existe'})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('artwork_list')

    return render(request, 'accounts/register.html')


# Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('artwork_list')
        else:
            return render(request, 'accounts/login.html', {'error': 'Credenciales inválidas'})

    return render(request, 'accounts/login.html')


# Logout
def user_logout(request):
    logout(request)
    return redirect('artwork_list')
