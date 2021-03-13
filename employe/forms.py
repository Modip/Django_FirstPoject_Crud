from django import forms
from employe.models import Employe

class EmployeForm(forms.ModelForm):
    prenom = forms.CharField()
    nom = forms.CharField()
    email = forms.EmailField()
    fonction = forms.CharField()
    class Meta:
        model = Employe
        fields = "__all__"