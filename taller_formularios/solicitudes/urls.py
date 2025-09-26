from django.urls import path
from . import views

app_name = "solicitudes"

urlpatterns = [
    path("", views.crear_solicitud, name="inicio"),
    path("nueva/", views.crear_solicitud, name="nueva"),
    path("enviada/", views.enviada, name="enviada"),
]
