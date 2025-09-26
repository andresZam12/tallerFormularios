from django.contrib import admin
from .models import Solicitud

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ("asunto", "nombre_solicitante", "tipo_solicitud", "fecha_solicitud")
    search_fields = ("asunto", "nombre_solicitante", "documento", "correo")
    list_filter = ("tipo_solicitud", "fecha_solicitud")
