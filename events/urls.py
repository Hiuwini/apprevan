"""events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, include

from django.contrib.auth import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

from app.views import ParticipantesListado, ParticipanteDetalle, ParticipanteCrear, ParticipanteActualizar, ParticipanteEliminar
from app.views import EventosListado, EventoDetalle, EventoCrear, EventoActualizar, EventoEliminar
from app.views import BeneficiosListado, BeneficioCrear, BeneficioEliminar

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': ''}),

    path('participantes/', ParticipantesListado.as_view(template_name = "participantes/index.html"), name='p.leer'),
    path('participantes/detalle/<int:pk>', ParticipanteDetalle.as_view(template_name = "participantes/detalles.html"), name='p.detalles'),
    path('participantes/crear', ParticipanteCrear.as_view(template_name = "participantes/crear.html"), name='p.crear'),
    path('participantes/editar/<int:pk>', ParticipanteActualizar.as_view(template_name = "participantes/actualizar.html"), name='p.actualizar'),
    path('participantes/eliminar/<int:pk>', ParticipanteEliminar.as_view(), name='p.eliminar'),

    path('eventos/', EventosListado.as_view(template_name = "eventos/index.html"), name='e.leer'),
    path('eventos/detalle/<int:pk>', EventoDetalle.as_view(template_name = "eventos/detalles.html"), name='e.detalles'),
    path('eventos/crear', EventoCrear.as_view(template_name = "eventos/crear.html"), name='e.crear'),
    path('eventos/editar/<int:pk>', EventoActualizar.as_view(template_name = "eventos/actualizar.html"), name='e.actualizar'),
    path('eventos/eliminar/<int:pk>', EventoEliminar.as_view(), name='e.eliminar'),

    path('beneficios/', BeneficiosListado.as_view(template_name = "beneficios/index.html"), name='b.leer'),
    path('beneficios/crear', BeneficioCrear.as_view(template_name = "beneficios/crear.html"), name='b.crear'),
    path('beneficios/eliminar/<int:pk>', BeneficioEliminar.as_view(), name='b.eliminar'),

]
