from django.forms import ModelForm
from .models import Person

class EmployeForm(ModelForm):
    class Meta:
        model = Person
        fields = ['prenom','nom','email']
    # prenom = forms.CharField(max_length=30)
    # nom = forms.CharField(max_length=30)
    # email = forms.EmailField(max_length=120)