from django.forms import ModelForm
from employe.models import Employe

class EmployeForm(ModelForm):
    class Meta:
        model = Employe
        fields = "__all__"
   