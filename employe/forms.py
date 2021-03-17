from django import forms
from employe.models import Employe

class EmployeForm(forms.ModelForm):
    prenom = forms.CharField(max_length=20)
    nom = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)
    fonction = forms.CharField(max_length=20)
    class Meta:
        model = Employe
        fields = "__all__"