from django import forms
from proyecto_APP.models import Persona

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
