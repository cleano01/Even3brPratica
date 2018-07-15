from django.forms.widgets import ClearableFileInput
from django.forms import ModelForm
from gerador.models import Certificado
from django import forms

class CertificadoForm(ModelForm):
    
    class Meta:
        model= Certificado
        fields= '__all__'

