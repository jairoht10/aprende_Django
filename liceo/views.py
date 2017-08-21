# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Liceo
from .forms import LiceoForm
from base.models import Municipio, Parroquia

# Create your views here.


class LiceoCreate(CreateView):
    model = Liceo
    form_class = LiceoForm
    template_name = "liceo.registro.template.html"
    success_url = reverse_lazy('liceo_lista')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.nombre = form.cleaned_data['nombre']
        self.object.apellido = form.cleaned_data['apellido']
        self.object.cedula = form.cleaned_data['cedula']
        self.object.telefono = form.cleaned_data['telefono']
        self.object.correo = form.cleaned_data['correo']
        #parroquia = Parroquia.objects.get(pk = form.cleaned_data['parroquia'])
        self.object.parroquia = form.cleaned_data['parroquia']
        user = self.request.user
        self.object.user = user
        self.object.save()

        #Frente.objects.create(
         #   nombre = form.cleaned_data['frente_nombre'],
         #   persona = self.object,
         #   municipio = form.cleaned_data['municipio'],
            
         #   user = self.request.user
        #)

        return super(LiceoCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(LiceoCreate, self).form_invalid(form)

class LiceoList(ListView):
    model = Liceo
    template_name = "liceo.lista.template.html"

    def get_queryset(self):
        queryset = Liceo.objects.filter(user=self.request.user)
        return queryset