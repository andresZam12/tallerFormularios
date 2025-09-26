from django import forms
from django.core.validators import RegexValidator
from .models import Solicitud

solo_digitos = RegexValidator(r"^\d{7,15}$", "Ingrese solo números (7-15 dígitos).")

class SolicitudForm(forms.ModelForm):
    telefono = forms.CharField(validators=[solo_digitos])

    class Meta:
        model = Solicitud
        fields = [
            "nombre_solicitante", "documento", "correo", "telefono",
            "tipo_solicitud", "asunto", "descripcion",
            "fecha_solicitud", "archivo",
        ]
        widgets = {
            "fecha_solicitud": forms.DateInput(attrs={"type": "date"}),
            "descripcion": forms.Textarea(attrs={"rows": 4}),
        }
