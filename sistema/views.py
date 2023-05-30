from django.http.response import JsonResponse
from django.shortcuts import render
from contacto.models import nuevoUsuario, comunidades,unidades,propietario,residente
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

def list_comunidad(_request):
    comunidad=list(comunidades.objects.values())
    data={'comunidades':comunidad}
    return JsonResponse(data)     

def paginaComunidad(request):
    return render(request,'comunidades.html')

def paginaUnidad(request):
    return render(request,'propiedades.html')

def list_unidad(_request):
    unidad=list(unidades.objects.values())
    data={'unidades':unidad}
    return JsonResponse(data) 
def list_propietarios(_request):
    propietarios=list(propietario.objects.values())  
    data={'propietario':propietarios}
    return JsonResponse(data)
def paginaPropietarios(request):
    return render(request,'propietarios.html')     

def list_residentes(_request):
    residentes=list(residente.objects.values())
    data={'residente':residentes}
    return JsonResponse(data)
def paginaResidentes(request):
    return render(request,'residentes.html')            
            
