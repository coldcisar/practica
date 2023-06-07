
from django.shortcuts import render
from contacto.models import nuevoUsuario,Comunidades,Unidades,Propietario,Residente
from django.contrib import messages 


def paginaIndex(request):
    return render(request, 'index.html')

def paginaLogin(request):
    if request.method == 'POST':
        try:
            detalleUsuario=nuevoUsuario.objects.get(usuario=request.POST['usuario'],contraseña=request.POST['contraseña'])
            print("Usuario=",detalleUsuario)
            request.session['usuario']=detalleUsuario.usuario
            return render(request, 'index.html')
        except nuevoUsuario.DoesNotExist as e:
            messages.success(request,'Usuario no existe')
    return render(request, 'inicio.html')

def cerrar_sesion(request):
    template_name='inicio.html'
    return render(request, template_name)

def list_comunidad(request):
    template_name='comunidades.html'
    comunidades=Comunidades.objects.all()
    context={
        "comunidades": comunidades
    }
    return render(request, template_name,context)    

def list_propietarios(request):
    template_name='propietarios.html'
    propietarios=Propietario.objects.all()
    context={
        "propietarios": propietarios
    }
    return render(request, template_name,context)   
def list_residentes(request):
    template_name='residentes.html'
    residentes=Residente.objects.all()
    context={
        "residentes": residentes
    }
    return render(request, template_name,context)     

def list_unidad(request):
    template_name='propiedades.html'
    unidad=Unidades.objects.all()
    context={
        "unidad": unidad
    }
    return render(request, template_name,context)   
         
            
