from django.shortcuts import render,redirect
from django.http import HttpResponse
from employeur.forms import EmployeurForm
from .forms import EmployeurForm
from .models import Employeur

# def listEmployeur(request):
#     return HttpResponse('Hello Modip')
def listEmployeur(request):
    employeurs = Employeur.objects.all()
    context={
        'employeurs':employeurs
        }
    return render(request, 'employeur/employeur.html',context)


def addEmployeur(request):
    if request.method == "POST":
        form = EmployeurForm(request.POST)
        if form.is_valid():
            obj = Employeur()
            obj.nom = form.cleaned_data['nom']
            obj.email = form.cleaned_data['email']
            obj.save()
        redirect("/employeurlist")            
    else:
        form = EmployeurForm()         
    return render(request, 'employeur/addemployeur.html', {'form':form}) 

def deleteEmployeur(request, id):
    Employeur = Employeur.objects.get(id=id)
    Employeur.delete()
    return render(request, 'employeur/deleteemployeur.html', {'form':form}) 

