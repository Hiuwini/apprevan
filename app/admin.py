from django.contrib import admin

# Register your models here.
from .models import Participante
from .models import Evento
from .models import Beneficio

admin.site.register(Participante)
admin.site.register(Evento)
admin.site.register(Beneficio)
