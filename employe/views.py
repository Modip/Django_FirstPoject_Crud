from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeForm
from .models import Employe

def home(request):
    return HttpResponse('Hello Modio')

def listEmploye(request):
    employes = Employe.objects.all()
    return render(request, 'employe/employe.html', {'employes': employes})

def addEmploye(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.nom = form.cleaned_data['prenom']
            data.email = form.cleaned_data['nom']
            data.email = form.cleaned_data['email']
            data.email = form.cleaned_data['fonction']
            print(data)
            data.save()
        return redirect("/")            
    else:
        form = EmployeForm()
    return render(request, 'employe/employe.html', {'form':form})

def editEmploye(request, id):
    employe = Employe.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {
        'employe': EmployeForm()
    }
    return render(request, 'employe/editemploye.html', context)

def deleteEmploye(request, id):
    employe = Employe.objects.get(id=id)
    if request.method == 'POST':
        employe.delete()
        return redirect("/")
    context = {
        'employe': employe
    }
    return render(request, 'employe/deleteemploye.html', context)
