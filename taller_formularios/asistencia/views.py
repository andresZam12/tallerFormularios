from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import AsistenciaForm

def registrar_asistencia(request):
    if request.method == "POST":
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("asistencia:hecho")
    else:
        form = AsistenciaForm()
    return render(request, "asistencia/form.html", {"form": form})

def hecho(request):
    return render(request, "asistencia/hecho.html")

