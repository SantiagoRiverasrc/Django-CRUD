from django.shortcuts import render,redirect
from .models import curso
# Create your views here.


def gestor_cursos(request):
    cursito = curso.objects.all()
    return render(request, 'gestor.html', {
        'cur': cursito
    })


def registercurse(request):
    codigo=request.POST['textcodigo']
    nombre=request.POST['textnombre']
    creditos=request.POST['textcredito']
    
    registercurse = curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos
    )
    return redirect('/')


def edicioncurse(request, codigo):
    curse = curso.objects.get(codigo=codigo)
    return render(request, 'edicioncurso.html', {'curso': curse})


def editarcurso(request):
    codigo=request.POST['textcodigo']
    nombre=request.POST['textnombre']
    creditos=request.POST['textcredito']
    
    curse = curso.objects.get(codigo=codigo)
    curse.nombre = nombre
    curse.creditos = creditos
    curse.save()
    return redirect('/')
    
    
    

def eliminarcurse(request, codigo):
    curse = curso.objects.get(codigo=codigo)
    curse.delete()
    return redirect('/')
    
    