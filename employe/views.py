from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import EmployeForm
from .models import Employe

def home(request):
    return HttpResponse('Hello Modio')
@login_required(login_url='login')
def listEmploye(request):
    employes = Employe.objects.all()
    return render(request, 'employe/employe.html', {'employes': employes})

def addEmploye(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")            
    else:
        form = EmployeForm()
    return render(request, 'employe/addemploye.html', {'form':form})

def editEmploye(request, id):
    employe = Employe.objects.get(id=id)
    form=EmployeForm(instance=employe)
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
    employe.delete()
    return redirect("/")
    context = {
        'employe': employeForm()
    }
    return render(request, 'employe/deleteemploye.html', context)
