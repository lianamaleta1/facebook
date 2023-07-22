from django.contrib import admin

# Register your models here.
from .models import *
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'negocio', 'cuentaFac')
    list_filter = ('nombre', 'negocio')

admin.site.register(publicacion,PublicacionAdmin)