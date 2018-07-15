from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from gerador.models import Certificado
from gerador.forms import CertificadoForm

# Create your views here.

def index(request):
    if(request.method == 'POST'):
        print('um')
        form= CertificadoForm(request.POST, request.FILES)
        print(form.is_valid())
        if (form.is_valid()):
            print('dois')
            form.save()
            context={'form':form} 
            return render(request, 'gerador/index.html',context)
    form= CertificadoForm()
    context={'form':form} 
    return render(request, 'gerador/index.html',context)    