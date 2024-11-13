from django.shortcuts import render, redirect, get_object_or_404

from notasproyecto.forms import NotaForm
from notasproyecto.models import Nota


# Create your views here.

def lista_notas(request):
    notas = Nota.objects.all().order_by('-fecha_creacion')
    return render(request, 'lista_notas.html', {'notas': notas})

def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()
    return render(request, 'editar_nota.html', {'form': form})

def editar_nota(request, id):
    nota = get_object_or_404(Nota, id=id)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'editar_nota.html', {'form': form})

def eliminar_nota(request, id):
    nota = get_object_or_404(Nota, id=id)
    if request.method == 'POST':
        nota.delete()
        return redirect('lista_notas')
    return render(request, 'eliminar_nota.html', {'nota': nota})
