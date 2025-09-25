from django.contrib import admin

from django.contrib import admin
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "documento", "fecha_asistencia", "presente")
    search_fields = ("nombre_completo", "documento", "correo")
    list_filter = ("fecha_asistencia", "presente")
