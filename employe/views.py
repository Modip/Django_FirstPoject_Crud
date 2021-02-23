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
            emp = Employe()
            emp.nom = form.cleaned_data['prenom']
            emm.email = form.cleaned_data['nom']
            obj.email = form.cleaned_data['email']
            emp.email = form.cleaned_data['fonction']
            emp.save()
        redirect("/employelist")            
    else:
        form = EmployeurForm()         
    return render(request, 'employe/employe.html', {'form':form} ) 

def deleteEmploye(request, id):
    employe = Employe.objects.get(id=id)
    employe.delete()
    return render(request, 'employe/employedelete.html') 

