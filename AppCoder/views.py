from django.shortcuts import render
from .models import Curso, Profesor ,Estudiante, Entregable
from .forms import ProfesorForm, EstudianteForm, EntregableForm, CursoForm
from django.http import HttpResponse

# Create your views here.

#def crear_curso(request):
#    nombre_curso="Programacion"
#    comision_curso=10010
#    print("Creando curso")
#    curso=Curso(nombre=nombre_curso, comision=comision_curso)
#    curso.save()
#    respuesta=f"Curso creado--- {nombre_curso} - {comision_curso}"
#    return HttpResponse(respuesta)

    
def cursos(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = Curso()
            curso.nombre = form.cleaned_data['nombre']
            curso.comision = form.cleaned_data['comision']
            curso.save()
            form = CursoForm()
    else:
        form = CursoForm()

    cursos = Curso.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
    context = {"cursos": cursos, "form" : form}
    return render(request, "AppCoder/cursos.html", context)

def profesores(request):

    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor()
            profesor.nombre = form.cleaned_data['nombre']
            profesor.apellido = form.cleaned_data['apellido']
            profesor.email = form.cleaned_data['email']
            profesor.profesion = form.cleaned_data['profesion']
            profesor.save()
            form = ProfesorForm()
    else:
        form = ProfesorForm()

    profesores = Profesor.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
    context = {"profesores": profesores, "form" : form}
    return render(request, "AppCoder/profesores.html", context)

def estudiantes(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = Estudiante()
            estudiante.nombre = form.cleaned_data['nombre']
            estudiante.apellido = form.cleaned_data['apellido']
            estudiante.email = form.cleaned_data['email']
            estudiante.save()
            form = EstudianteForm()
    else:
        form = EstudianteForm()
    
    estudiantes = Estudiante.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
    context = {"estudiantes": estudiantes, "form" : form}
    return render(request, "AppCoder/estudiantes.html", context)

def entregables(request):
    if request.method == "POST":
        form = EntregableForm(request.POST)
        if form.is_valid():
            entregable = Entregable()
            entregable.nombre = form.cleaned_data['nombre']
            entregable.fecha_entrega = form.cleaned_data['fecha_entrega']
            entregable.entregado = form.cleaned_data['entregado']
            entregable.save()
            form = EntregableForm()
    else:
        form = EntregableForm()
    
    entregables = Entregable.objects.all() #Entregable.objects.filter(nombre__icontains="P").all()
    context = {"entregables": entregables, "form" : form}
    return render(request, "AppCoder/entregables.html", context)

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html")