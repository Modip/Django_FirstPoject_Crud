from django import forms
from employeur.models import Employeur
class EmployeurForm(forms.Form):
    nom = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=150)
    class Meta:
        model = Employeur
        fields = "__all__"

    