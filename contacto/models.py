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

class Comunidades(models.Model):
    nombre_comunidades = models.CharField(max_length=50)
    tipo_comunidades = models.CharField(max_length=20,choices= tipos,default='Condominio',null=True)
    direccion_comunidades = models.CharField(max_length=50)
    conserje_nombre= models.CharField(max_length=50)
    fono_comunidades = models.IntegerField()
    n_unidades= models.IntegerField()
    n_residentes=models.IntegerField()

    class Meta:
        verbose_name = "Comunidad"
        verbose_name_plural ="Comunidades"
        db_table ='comunidades' 

    def __str__(self):
        return self.nombre_comunidades      

class Id_residente(models.Model):
    residente=models.CharField(max_length=9)

    class Meta:
        verbose_name = 'id_residente'
        verbose_name_plural = 'id_residentes'
        db_table ='id_residentes'

    def __str__(self):
        return str(self.residente)    

class Id_propietario(models.Model):
    propietario=models.CharField(max_length=9) 
    
    class Meta:
        verbose_name = 'id_propietario'
        verbose_name_plural = 'id_propietarios'
        db_table ='id_propietarios'

    def __str__(self):
        return str(self.id)
 

class Id_conserje(models.Model):
    propietario=models.CharField(max_length=9) 
    
    class Meta:
        verbose_name = 'id_conserje'
        verbose_name_plural = 'id_conserje'
        db_table ='id_conserje'

    def __str__(self):
        return str(self.conserje)     


class Unidades(models.Model):
    n_recinto=models.CharField(max_length=50,verbose_name='unidad')
    tipo_unidad = models.CharField(max_length=13,choices=tiposU,default='Casa')
    nombre_villa=models.ForeignKey(Comunidades,null=True,blank=True,on_delete=models.CASCADE,related_name='nombre_villa')
    direccion_unidad=models.CharField(max_length=50)
    propietario=models.ForeignKey(Id_propietario,null=True,blank=True,on_delete=models.CASCADE,related_name='propietario_id')
    telefono_propietario=models.ForeignKey(Id_propietario,null=True,blank=True,on_delete=models.CASCADE,related_name='telefono_propietario')
    comunidad=models.ForeignKey(Comunidades,null=True,blank=True,on_delete=models.CASCADE,related_name='comununidad')
    
    class Meta:
        verbose_name ='Unidade'
        verbose_name_plural ='Unidades'
        db_table ='unidades'

    def __str__(self):
        return str(self.n_recinto)



class Residente(models.Model):
    rut_residente=models.ForeignKey(Id_residente, null=True,blank=True,on_delete=models.CASCADE,related_name='residentesID')
    tipo_unidad_residente=models.CharField(max_length=15,null=True,choices=tiposU)
    direccion=models.CharField(max_length=50)
    n_recinto=models.ForeignKey(Unidades,null=True,blank=True,on_delete=models.CASCADE,related_name='n_recinto_residente')
    rut_propietario=models.ForeignKey(Id_propietario,null=True,blank=True,on_delete=models.CASCADE,related_name='propietarioID')
    telefono_residente=models.IntegerField()
    estado_r=models.CharField(max_length=10,null=True)

    class Meta:
        verbose_name="Residente"
        verbose_name_plural="Residentes"
        db_table="residentes"

    def __str__(self):
        return str(self.rut_residente)    

   
class Propietario(models.Model):
    rut_propietario=models.ForeignKey(Id_propietario,null=True,blank=True,on_delete=models.CASCADE,related_name="rut_propietario")
    tipo_unidad=models.CharField(max_length=15,null=True,choices=tiposU)
    direccion=models.CharField(max_length=50)
    n_recinto=models.ForeignKey(Unidades,null=True,blank=True,on_delete=models.CASCADE,related_name='n_recinto_propietario')
    rut_residente=models.ForeignKey(Id_residente, null=True,blank=True,on_delete=models.CASCADE,related_name='rut_residente')
    telefono_propietario=models.IntegerField()
    estado=models.CharField(max_length=10)

    class Meta:
        verbose_name = "Propietario"
        verbose_name_plural = "Propietarios"
        db_table = "propietarios"
    
    def __str__(self):
        return str(self.rut_propietario)   

class Conserje(models.Model):
    rut_conserje=models.CharField(max_length=10,null=True)
    nombre_apellido=models.CharField(max_length=50)
    fono_conserje=models.IntegerField()
    comunidad=models.ForeignKey(Comunidades,null=True,blank=True,on_delete=models.CASCADE,related_name='comunidad')

    class Meta:
        verbose_name = "Conserje"
        verbose_name_plural ="Conserjes"
        db_table = "conserjes"

    def __str__(self):
        return str(self.rut_conserje)    

class Bodegas(models.Model):
    n_bodega=models.CharField(max_length=5)
    n_recinto_bodegas=models.ForeignKey(Unidades,null=True,blank=True,on_delete=models.CASCADE,related_name='n_recinto_bodegas')
    comunidad_bodegas = models.ForeignKey(Comunidades,null=True,blank=True,on_delete=models.CASCADE,related_name='comunidad_bodegas')

    class Meta:
        verbose_name = "Bodega"
        verbose_name_plural ="Bodegas"
        db_table = "bodegas"

    def __str__(self):
        return str(self.n_bodega) 

class Estacionamiento(models.Model):
    n_estacionamiento=models.CharField(max_length=5)
    n_recinto_estacionamiento=models.ForeignKey(Unidades,null=True,blank=True,on_delete=models.CASCADE,related_name='n_recinto_estacionamiento')
    comunidad_estacionamiento = models.ForeignKey(Comunidades,null=True,blank=True,on_delete=models.CASCADE,related_name='comunidad_estacionamiento')

    class Meta:
        verbose_name = "Estacionamiento"
        verbose_name_plural ="Estacionamientos"
        db_table = "estacionamientos"

    def __str__(self):
        return str(self.n_estacionamiento) 






