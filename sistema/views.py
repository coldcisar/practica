
from django.shortcuts import render,redirect
from contacto.models import nuevoUsuario,Comunidades,Unidades,Propietario,Residente,Conserje,Estacionamiento,Bodegas,Id_propietario
from django.contrib import messages 
from django.http import HttpResponseRedirect


def paginaIndex(request):
    return render(request, 'index.html')
def paginaAgregar(request):
    return render(request, 'agregarC.html')
def agregarC(request):
    if request.method == 'POST':
        if request.POST.get('nombreC')and request.POST.get('tipoC')and request.POST.get('DireccionComunidad')and request.POST.get('ConserjeID')and request.POST.get('FonoComunidad')and request.POST.get('n_unidad')and request.POST.get('n_residentes'):
            comunidad=Comunidades()
            comunidad.nombre_comunidades=request.POST.get('nombreC')
            comunidad.tipo_comunidades=request.POST.get('tipoC')
            comunidad.direccion_comunidades=request.POST.get('DireccionComunidad')
            comunidad.conserje_nombre=request.POST.get('ConserjeID')
            comunidad.fono_comunidades=request.POST.get('FonoComunidad')
            comunidad.n_unidades=request.POST.get('n_unidad')
            comunidad.n_residentes=request.POST.get('n_residentes')
            comunidad.save()
            return redirect('list_comunidad')
    else:
        return render(request,"agregarC.html")    

def actualizarC(request,idComunidades):
    try:
        if request.method == 'POST':
            if request.POST.get('nombreC')and request.POST.get('tipoC')and request.POST.get('DireccionComunidad')and request.POST.get('ConserjeID')and request.POST.get('FonoComunidad')and request.POST.get('n_unidad')and request.POST.get('n_residentes'):
                comunidad_id_old=request.POST.get('nombreC')    
                comunidad_old=Comunidades()
                comunidad_old=Comunidades.objects.get(nombre_comunidades=comunidad_id_old)

                comunidad=Comunidades()
                comunidad.nombre_comunidades=request.POST.get('nombreC')
                comunidad.tipo_comunidades=request.POST.get('tipoC')
                comunidad.direccion_comunidades=request.POST.get('DireccionComunidad')
                comunidad.conserje_nombre=request.POST.get('ConserjeID')
                comunidad.fono_comunidades=request.POST.get('FonoComunidad')
                comunidad.n_unidades=request.POST.get('n_unidad')
                comunidad.n_residentes=request.POST.get('n_residentes')
                comunidad.save()
                return redirect('list_comunidad')
        else:      
            comunidades=Comunidades.objects.all()
            comunidad=Comunidades.objects.get(nombre_comunidades=idComunidades)
            datos={'comunidades':comunidades, "comunidad":comunidad}
            return render(request, 'actualizarC.html', datos)

        
    except Comunidades.DoesNotExist:
        comunidades=Comunidades.objects.all()
        comunidad=None
        datos={'comunidades':comunidades, "comunidad":comunidad}
        return render(request, 'actualizarC.html', datos)
    
def propietarios_ID(request,idPropietario):
    try:
        propietarios=Propietario.objects.all()
        propietario=Propietario.objects.get(id=idPropietario)
        datos={'propietarios': propietarios,"propietario": propietario}
        if propietario != None :
            return render(request,"propietario_unidad.html",datos)  
    except Propietario.DoesNotExist:
        return render(request,"propiedades.html")
    

def actualizarP(request):
    if request.method == "POST":
        propietario= Propietario.objects.get(id=request.POST.get('id'))
        if propietario != None :
            propietario.rut_propietario=request.POST.get('rut_propietario')
            propietario.tipo_unidad=request.POST.get('tipo_unidad')
            propietario.direccion=request.POST.get('direccion')
            propietario.n_recinto=request.POST.get('n_recinto')
            propietario.rut_residente=request.POST.get('rut_residente')
            propietario.telefono_propietario=request.POST.get('telefono_propietario')
            propietario.estado=request.POST.get('estado')
            if request.POST.get('estado')=="Inactivo":
                return redirect("propietarios_historicos.html")
            propietario.save()
            messages.success(request,"Propietario Actualizado Correctamente")
            return HttpResponseRedirect("/")


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
def list_propietarios_historicos(request):
    template_name='propietarios_historicos.html'
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

def list_conserje(request):
    template_name='conserje.html'
    conserje=Conserje.objects.all()
    context={
        'conserjes':conserje
    }    
    return render(request, template_name,context)

def list_estacionamiento(request):
    template_name='estacionamiento.html'
    estacionamiento=Estacionamiento.objects.all()
    context={
        'estacionamiento':estacionamiento
    }    
    return render(request, template_name,context)
def list_bodegas(request):
    template_name='bodegas.html'
    bodegas=Bodegas.objects.all()
    context={
        'bodega':bodegas
    }    
    return render(request, template_name,context)


         
            
