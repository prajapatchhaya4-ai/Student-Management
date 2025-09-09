from django import forms
from .models import Student
class Stdform(forms.ModelForm):
    class Meta:
        model=Student
        fields ="__all__"

