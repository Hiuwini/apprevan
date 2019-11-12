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


class ParticipantesListado(ListView):
    model = Participante

class ParticipanteCrear(SuccessMessageMixin, CreateView):
    model = Participante
    form = Participante
    fields = "__all__"
    success_message = 'Participante creado correctamente'

    def get_success_url(self):
        return reverse('p.leer')

class ParticipanteDetalle(DetailView):
    model = Participante

class ParticipanteActualizar(SuccessMessageMixin, UpdateView):
    model = Participante
    form = Participante
    fields = "__all__"
    success_message = 'Participante actualizado correctamente'

    def get_success_url(self):
        return reverse('p.leer')

class ParticipanteEliminar(SuccessMessageMixin, DeleteView):
    model = Participante
    form = Participante
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Participante eliminado correctamente'
        messages.success (self.request, (success_message))
        return reverse('p.leer')

class EventosListado(ListView):
    model = Evento

class EventoCrear(SuccessMessageMixin, CreateView):
    model = Evento
    form = Evento
    fields = "__all__"
    success_message = 'Evento creado correctamente'

    def get_success_url(self):
        return reverse('e.leer')

class EventoDetalle(DetailView):
    model = Evento

class EventoActualizar(SuccessMessageMixin, UpdateView):
    model = Evento
    form = Evento
    fields = "__all__"
    success_message = 'Evento actualizado correctamente'

    def get_success_url(self):
        return reverse('e.leer')

class EventoEliminar(SuccessMessageMixin, DeleteView):
    model = Evento
    form = Evento
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Evento eliminado correctamente'
        messages.success (self.request, (success_message))
        return reverse('e.leer')

class BeneficiosListado(ListView):
    model = Evento

class BeneficioDetalle(DetailView):
    model = Beneficio.objects.select_related('e_id')
