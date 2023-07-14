"""sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/',views.paginaIndex,name='menu'),
    path('',views.paginaLogin, name='paginaLogin'),
    path('list_comunidad/',views.list_comunidad,name='list_comunidad'),
    path('list_unidad/',views.list_unidad,name='list_unidad'),
    path('list_propietarios/',views.list_propietarios,name='list_propietarios'),
    path('list_residentes/',views.list_residentes,name='list_residentes'),
    path('login',views.cerrar_sesion,name='cerrar_sesion'),
    path('agregar_comunidad',views.agregarC,name='agregar_comunidad'),
    path('actualizar_comunidad/<idComunidades>',views.actualizarC,name='actualizar_comunidad'),
    path('list_conserjes/',views.list_conserje,name='list_conserjes'),
    path('list_estacionamiento/',views.list_estacionamiento,name='list_estacionamiento'),
    path('list_bodegas/',views.list_bodegas,name='list_bodegas'),
    path('propietarios_unidad/<idPropietario>',views.propietarios_ID,name='propietarios_unidad'),
    path('list_medidores/',views.list_medidores,name="list_medidores"),
    path('list_residentes_temporales/',views.list_residentes_temporales,name='list_residentes_temporales'),
    path('list_proveedores/',views.list_proveedores,name='list_proveedores'),
    path('list_actasO/',views.list_actasO,name='list_actasO'),
    path('list_actasE/',views.list_actasE,name='list_actasE'),
    path('list_bitacoras/',views.list_bitacora,name='list_bitacoras')
    
]
