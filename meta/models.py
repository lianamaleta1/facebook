from django.db import models

# Create your models here.

class facebookapi(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    siglas = models.CharField(max_length=200, blank=True, verbose_name="Siglas")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Facebookapi'
        verbose_name_plural = 'Facebookapi'
        db_table = 'Facebookapi'

    def __str__(self):
        return f"{self.nombre}"

class cuentas(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    nombreGrupo=models.CharField(max_length=100, unique=True,verbose_name="Grupo")
    nombrePagina = models.CharField(max_length=100, unique=True,verbose_name="Pagina")
    linkGrupo= models.URLField(on_delete=models.DO_NOTHING, null=True, blank=True)
    linkPaginas = models.URLField( on_delete=models.DO_NOTHING, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        db_table = 'cuenta'

    def __str__(self):
        return f"{self.nombre}"

class publicacion(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    negocio=models.CharField(max_length=100, unique=True,verbose_name="Negocio")
    cuentaFac = models.ForeignKey(cuentas,on_delete=models.DO_NOTHING,max_length=100, unique=True)
    texto=models.CharField(max_length=500, unique=True)
    imagen_logo = models.ImageField(upload_to='imagenes/', blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        db_table = 'cuenta'

    def __str__(self):
        return f"{self.nombre}"
