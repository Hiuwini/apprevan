from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Participante
from .models import Evento
from .models import Beneficio

from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, Template
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.apps import apps
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
import datetime, locale
from datetime import  timedelta
from django.db import IntegrityError
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='login'),name="dispatch")
class ParticipantesListado(ListView):
    model = Participante

@method_decorator(login_required(login_url='login'),name="dispatch")
class ParticipanteCrear(SuccessMessageMixin, CreateView):
    model = Participante
    form = Participante
    fields = "__all__"
    success_message = 'Participante creado correctamente'

    def get_success_url(self):
        return reverse('p.leer')

@method_decorator(login_required(login_url='login'),name="dispatch")
class ParticipanteDetalle(DetailView):
    model = Participante

@method_decorator(login_required(login_url='login'),name="dispatch")
class ParticipanteActualizar(SuccessMessageMixin, UpdateView):
    model = Participante
    form = Participante
    fields = "__all__"
    success_message = 'Participante actualizado correctamente'

    def get_success_url(self):
        return reverse('p.leer')

@method_decorator(login_required(login_url='login'),name="dispatch")
class ParticipanteEliminar(SuccessMessageMixin, DeleteView):
    model = Participante
    form = Participante
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Participante eliminado correctamente'
        messages.success (self.request, (success_message))
        return reverse('p.leer')

@method_decorator(login_required(login_url='login'),name="dispatch")
class EventosListado(ListView):
    model = Evento

@method_decorator(login_required(login_url='login'),name="dispatch")
class EventoCrear(SuccessMessageMixin, CreateView):
    model = Evento
    form = Evento
    fields = "__all__"
    success_message = 'Evento creado correctamente'

    def get_success_url(self):
        return reverse('e.leer')

@method_decorator(login_required(login_url='login'),name="dispatch")
class EventoDetalle(DetailView):
    model = Evento

@method_decorator(login_required(login_url='login'),name="dispatch")
class EventoActualizar(SuccessMessageMixin, UpdateView):
    model = Evento
    form = Evento
    fields = "__all__"
    success_message = 'Evento actualizado correctamente'

    def get_success_url(self):
        return reverse('e.leer')

@method_decorator(login_required(login_url='login'),name="dispatch")
class EventoEliminar(SuccessMessageMixin, DeleteView):
    model = Evento
    form = Evento
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Evento eliminado correctamente'
        messages.success (self.request, (success_message))
        return reverse('e.leer')

@method_decorator(login_required(login_url='login'),name="dispatch")
class BeneficiosListado(ListView):
    model = Beneficio

@method_decorator(login_required(login_url='login'),name="dispatch")
class BeneficioCrear(SuccessMessageMixin, CreateView):
    model = Beneficio
    form = Beneficio
    fields = "__all__"
    success_message = 'Beneficio creado correctamente'

    def get_success_url(self):
        return reverse('b.leer')

@method_decorator(login_required(login_url='login'),name="dispatch")
class BeneficioEliminar(SuccessMessageMixin, DeleteView):
    model = Beneficio
    form = Beneficio
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Beneficio eliminado correctamente'
        messages.success (self.request, (success_message))
        return reverse('b.leer')
