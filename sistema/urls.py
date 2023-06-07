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

]
