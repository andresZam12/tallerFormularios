from django.db import models

TIPOS_SOLICITUD = [
    ("academica", "Académica"),
    ("administrativa", "Administrativa"),
    ("tecnica", "Técnica"),
    ("otra", "Otra"),
]

class Solicitud(models.Model):
    nombre_solicitante = models.CharField(max_length=150)
    documento = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)  # CharField para conservar ceros
    tipo_solicitud = models.CharField(max_length=20, choices=TIPOS_SOLICITUD)
    asunto = models.CharField(max_length=120)
    descripcion = models.TextField()
    fecha_solicitud = models.DateField()
    archivo = models.FileField(upload_to="solicitudes/", blank=True, null=True)

    def __str__(self):
        return f"[{self.asunto}] - {self.nombre_solicitante}"
