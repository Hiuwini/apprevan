from django.urls import path

from app.views import ParticipantesListado, ParticipanteDetalle, ParticipanteCrear, ParticipanteActualizar, ParticipanteEliminar
from app.views import EventosListado, EventoDetalle, EventoCrear, EventoActualizar, EventoEliminar
from app.views import BeneficiosListado, BeneficioCrear, BeneficioEliminar

from . import views

urlpatterns = [
    path('', ParticipantesListado.as_view(template_name = "participantes/index.html"), name='p.leer'),
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
