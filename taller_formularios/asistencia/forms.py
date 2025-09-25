from django import forms
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = [
            "nombre_completo", "documento", "correo",
            "fecha_asistencia", "hora_ingreso", "hora_salida",
            "presente", "observaciones",
        ]
        widgets = {
            "fecha_asistencia": forms.DateInput(attrs={"type": "date"}),
            "hora_ingreso": forms.TimeInput(attrs={"type": "time"}),
            "hora_salida": forms.TimeInput(attrs={"type": "time"}),
            "observaciones": forms.Textarea(attrs={"rows": 3}),
        }
