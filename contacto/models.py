from django.db import models
from .choices import tipos,tiposU

class nuevoUsuario(models.Model):
    usuario=models.CharField(blank=True ,max_length=150,verbose_name="Usuario")
    contraseña=models.CharField(blank=True, max_length=150,verbose_name="Contraseña")

    def __str__(self):
        return self.usuario
    class Meta:
        ordering =['usuario'] 
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class comunidades(models.Model):
    nombre_comunidades = models.CharField(max_length=50)
    tipo_comunidades = models.CharField(max_length=20,choices= tipos,default='Condominio')
    direccion_comunidades = models.CharField(max_length=50)
    conserje_nombre= models.CharField(max_length=50)
    fono_comunidades = models.IntegerField()
    n_unidades= models.IntegerField()
    n_residentes=models.IntegerField()

    class Meta:
        verbose_name = "Comunidad"
        verbose_name_plural ="Comunidades"
        db_table ='comunidades'   

class id_residente(models.Model):
    residente=models.CharField(max_length=9)

    class Meta:
        verbose_name = 'id_residente'
        verbose_name_plural = 'id_residentes'
        db_table ='id_residentes'

class id_propietario(models.Model):
    propietario=models.CharField(max_length=9) 
    
    class Meta:
        verbose_name = 'id_propietario'
        verbose_name_plural = 'id_propietarios'
        db_table ='id_propietarios'


class unidades(models.Model):
    n_recinto=models.CharField(max_length=50,verbose_name='unidad')
    tipo_unidad = models.CharField(max_length=13,choices=tiposU,default='Casa')
    nombre_villa=models.ForeignKey(comunidades,null=True,blank=True,on_delete=models.CASCADE,related_name='nombre_villa')
    direccion_unidad=models.CharField(max_length=50)
    propetario=models.ForeignKey(id_propietario,null=True,blank=True,on_delete=models.CASCADE,related_name='propetario')
    telefono_propietario=models.ForeignKey(id_propietario,null=True,blank=True,on_delete=models.CASCADE,related_name='telefono_propetario')
    comunidad=models.ForeignKey(comunidades,null=True,blank=True,on_delete=models.CASCADE,related_name='comununidad')
    
    class Meta:
        verbose_name ='Unidade'
        verbose_name_plural ='Unidades'
        db_table ='unidades'



class residente(models.Model):
    rut_residente=models.ForeignKey(id_residente, null=True,blank=True,on_delete=models.CASCADE,related_name='residentesID')
    tipo_unidad_residente=models.ForeignKey(unidades,null=True,blank=True,on_delete=models.CASCADE,related_name='nombre_unidad')
    direccion=models.CharField(max_length=50)
    n_recinto=models.ForeignKey(unidades,null=True,blank=True,on_delete=models.CASCADE,related_name='n_recinto_residente')
    rut_propietario=models.ForeignKey(id_propietario,null=True,blank=True,on_delete=models.CASCADE,related_name='propietarioID')
    telefono_residente=models.IntegerField()

    class Meta:
        verbose_name="Residente"
        verbose_name_plural="Residentes"
        db_table="residentes"

   
class propietario(models.Model):
    rut_propietario=models.ForeignKey(id_propietario,null=True,blank=True,on_delete=models.CASCADE,related_name="rut_propietario")
    tipo_unidad=models.ForeignKey(unidades,null=True,blank=True,on_delete=models.CASCADE,related_name="tipo_unidad_propietario")
    direccion=models.CharField(max_length=50)
    n_recinto=models.ForeignKey(unidades,null=True,blank=True,on_delete=models.CASCADE,related_name='n_recinto_propietario')
    rut_residente=models.ForeignKey(id_residente, null=True,blank=True,on_delete=models.CASCADE,related_name='rut_residente')
    telefono_propetario=models.IntegerField()
    estado=models.CharField(max_length=10)

    class Meta:
        verbose_name = "Propietario"
        verbose_name_plural = "Propietarios"
        db_table = "propietarios"






