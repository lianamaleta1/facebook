from django.contrib import admin

# Register your models here.
from .models import *

class PublicacionAdmin(admin.ModelAdmin):
    inlines = [ImagenInline, GrupoInline]

admin.site.register(publicacion,PublicacionAdmin)

"""class facebookApiAdmin(admin.ModelAdmin):
    list_display = ('identificador','nombre','dominio','secreto')
admin.site.register(facebookapi,facebookApiAdmin)"""