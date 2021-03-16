from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import CreateUser

# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('employelist')
        else:
            messages.info(request, "Utilisateur et/ou mot de passe invalide")
    context = {

    }
    return render(request, 'accounts/login.html', context)

def registerUser(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.succes(request, 'Compte creer avec success '+user)
            return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)