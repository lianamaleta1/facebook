from django.db import models
from django.contrib import admin
from PIL import ImageFile
# Create your models here.

class facebookapi(models.Model):
    identificador = models.CharField(max_length=20, unique=True,default='')
    nombre = models.CharField(max_length=200, blank=True,default='')
    dominio=models.CharField(max_length=200, blank=True,default='')
    secreto = models.CharField(max_length=200, blank=True, default='')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Facebookapi'
        verbose_name_plural = 'Facebookapi'
        db_table = 'Facebookapi'

    def __str__(self):
        return f"{self.nombre}"

class cuenta(models.Model):
    usuario = models.CharField(max_length=20, unique=True,default="")
    passwor=models.CharField(max_length=50,default="")
    nombreGrupo=models.CharField(max_length=100,verbose_name="Grupo")
    nombrePagina = models.CharField(max_length=100, verbose_name="Pagina")
    linkGrupo= models.URLField(max_length=100, null=True, blank=True)
    linkPaginas = models.URLField( max_length=100, null=True, blank=True)


    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'cuenta'
        verbose_name_plural = 'Cuentas'
        db_table = 'cuenta'

    def __str__(self):
        return f"{self.nombre}"

class publicacion(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    negocio=models.CharField(max_length=100, verbose_name="Negocio")
    texto=models.CharField(max_length=500, )
    linkPaginas = models.URLField(max_length=100, null=True, blank=True)
    frecpublicacion=models.FloatField(default=24.0)
    lastPOST=models.IntegerField()
    activa=models.BooleanField(default='false')


    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'publicacion'
        verbose_name_plural = 'publicacion'
        db_table = 'publicacion'

    def __str__(self):
        return f"{self.nombre}"

class imagen(models.Model):
    imagen = models.ImageField(upload_to='image/')
    publicacion = models.ForeignKey(publicacion,on_delete=models.CASCADE,max_length=100)

class grupo(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Grupo")
    publicacion = models.ForeignKey(publicacion,on_delete=models.CASCADE,max_length=100)

class GrupoInline(admin.StackedInline):
    model = grupo

class ImagenInline(admin.TabularInline):
    model = imagen

#class ImagenInline(admin.StackedInline):
    #model = imagen

  