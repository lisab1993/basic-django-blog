from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            user = User.objects.create_user(
                username=username,
                password=password1
            )
            login(request, user)
            return redirect('chirpapp:index')
    return render(request, 'users/register.html')

#this view can't be called login because we're already importing login from django.contrib.auth 
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('chirpapp:index')
        else:
            print('Oops, something went wrong')
    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return render(request, 'users/login.html')