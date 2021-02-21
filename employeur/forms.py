from django import forms

class EmployeurForm(forms.Form):
    nom = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=150)