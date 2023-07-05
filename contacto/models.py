from django.db import models
from .choices import tipos,tiposU,estados,tiposM

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
        return str(self.propietario)

     


class Unidades(models.Model):
    n_recinto=models.CharField(max_length=50,verbose_name='unidad')
    tipo_unidad = models.CharField(max_length=13,choices=tiposU,default='Casa')
    nombre_villa=models.ForeignKey(Comunidades,null=True,blank=True,on_delete=models.CASCADE,related_name='nombre_villa')
    direccion_unidad=models.CharField(max_length=50)
    propietario=models.ForeignKey(Id_propietario,null=True,blank=True,on_delete=models.CASCADE,related_name='propietario_id')
    telefono_propietario=models.CharField(max_length=9,null=True)
    comunidad=models.ForeignKey(Comunidades,null=True,blank=True,on_delete=models.CASCADE,related_name='comununidad')
    grupo=models.CharField(max_length=50,null=True)
    
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
    estado_r=models.CharField(max_length=10,null=True,choices=estados)

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
    estado=models.CharField(max_length=10,choices=estados)

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
    

class Medidores(models.Model):
    n_medidor=models.IntegerField()
    tipo_medidor=models.CharField(max_length=10,choices=tiposM)
    comunidad_medidor=models.ForeignKey(Comunidades, null=True, blank=True, on_delete=models.CASCADE,related_name='comunidad_medidor')

    class Meta:
        verbose_name = "Medidor"
        verbose_name_plural ="Medidores"
        db_table = "medidores"

    def __str__(self):
        return str(self.n_medidor) 

class ResidentesT(models.Model):
    rut_residenteT=models.ForeignKey(Id_residente, null=True,blank=True,on_delete=models.CASCADE,related_name='residentestID')
    tipo_unidad_residenteT=models.CharField(max_length=15,null=True,choices=tiposU)
    direccionT=models.CharField(max_length=50)
    n_recintoT=models.ForeignKey(Unidades,null=True,blank=True,on_delete=models.CASCADE,related_name='n_recinto_residenteT')
    rut_propietarioT=models.ForeignKey(Id_propietario,null=True,blank=True,on_delete=models.CASCADE,related_name='propietariotID')
    telefono_residentTe=models.IntegerField()
    estado_rT=models.CharField(max_length=10,null=True,choices=estados)
    fecha_inicio=models.DateTimeField()
    fecha_fin=models.DateTimeField()

    class Meta:
        verbose_name="ResidenteT"
        verbose_name_plural="ResidentesT"
        db_table="residentesT"

    def __str__(self):
        return str(self.rut_residenteT) 

class Proveedores(models.Model):
    rut_proveedores=models.CharField(max_length=10,null=True)
    nombre_proveedor=models.CharField(max_length=50,null=True)
    comunidad_proveedores=models.ForeignKey(Comunidades,null=True,blank=True,on_delete=models.CASCADE,related_name="comunidad_proveedores")

    class Meta:
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"
        db_table = "proveedores"
    def __str__(self):
        return str(self.rut_proveedores)    

class ActasO(models.Model):
    id_actasO=models.CharField(max_length=5,null=True)
    asunto=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=150)

    class Meta:
        verbose_name= "actaO"
        verbose_name_plural= "actasO"
        db_table= "actasO"

    def __str__(self):
        return str(self.id_actasO)
        
class ActasE(models.Model):
    id_actasE=models.CharField(max_length=5)
    asuntoE=models.CharField(max_length=20)
    descripcionE=models.CharField(max_length=150)

    class Meta:
        verbose_name = "actaE"
        verbose_name_plural = "actasE"
        db_table = "actasE"

    def __str__(self):
        return str(self.id_actasE)

class Bitacora(models.Model):
    id_bitacora=models.CharField(max_length=5)
    nombre_bitacora=models.CharField(max_length=20)
    comunidad_bitacora=models.ForeignKey(Comunidades, null=True, blank=True,on_delete=models.CASCADE,related_name="comunidad_bitacora")

    class Meta:
        verbose_name = "bitacora"
        verbose_name_plural ="bitacoras"
        db_table="bitacoras"

    def __str__(self):
        return str(self.id_bitacora)









