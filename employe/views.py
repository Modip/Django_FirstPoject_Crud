from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeForm
from .models import Person

# Create your views here.
def crud(request):
    return render(request, 'templates/index.html')
    
def employe(request):
    if request.method == 'POST':
        data = request.POST
        prenom = data['prenom']
        nom = data['nom']
        email = data['email']

        obj = Person.objects.create(prenom=prenom,nom=nom,email=email)
        if obj:
            return redirect('/employe') 
            return HttpResponse("Erreur lors de l'ajout")    
    else:
        form = EmployeForm()
        context = {
            'form':form
        } 
    return render(request,'employe/employe.html',context)    