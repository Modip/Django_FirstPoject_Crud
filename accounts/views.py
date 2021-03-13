from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .forms import LoginForm

# Create your views here.

def LoginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
        print(user)
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login/login.html', context)

def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(username=data['username'], password=data['password1'])
            user.save()
            return redirect('/')
    form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)