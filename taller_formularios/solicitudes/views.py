from django.shortcuts import render, redirect
from .forms import SolicitudForm

def crear_solicitud(request):
    if request.method == "POST":
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("solicitudes:enviada")
    else:
        form = SolicitudForm()
    return render(request, "solicitudes/form.html", {"form": form})

def enviada(request):
    return render(request, "solicitudes/enviada.html")
