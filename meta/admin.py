from django.contrib import admin
# Register your models here.
from .models import *
from .views import *
from django.contrib import messages

class GrupoInline(admin.TabularInline):
    model = grupo

class ImagenInline(admin.TabularInline):
    model = imagen

class PublicacionAdmin(admin.ModelAdmin):
    inlines = [ImagenInline, GrupoInline]

admin.site.register(publicacion,PublicacionAdmin)


def tokenLargoUsario(modeladmin, request, queryset):
    if queryset.count() != 1:
        messages.error(request, 'Esta acción solo se puede ejecutar seleccionando un objeto.')
        return

    instance = queryset.first()
    try:
        social_app = SocialApp.objects.get(provider='facebook')
        social_meta = facebookapi.objects.get(pk=social_app.id)

        app_id = social_app.client_id
        app_secret = social_app.secret
        short_token = social_meta.token_acceso

        # Realiza una solicitud GET para obtener el token de acceso de larga duración
        response = requests.get(f'https://graph.facebook.com/v13.0/oauth/access_token?grant_type=fb_exchange_token&client_id={app_id}&client_secret={app_secret}&fb_exchange_token={short_token}')

        # Analiza la respuesta JSON
        data = response.json()

        # Extrae el token de acceso de larga duración
        long_token = data['access_token']

        # Actualiza el objeto con el token de acceso de larga duración
        instance.token_largo = long_token
        instance.save()

        messages.success(request, f'Token de acceso de larga duración obtenido y guardado en el objeto.')
    except (SocialApp.DoesNotExist, facebookapi.DoesNotExist):
        messages.error(request, 'Error al obtener el token de acceso de larga duración.')

        obtener_token_largo.short_description = 'Obtener Token de Acceso de Larga Duración (Ejecutar una vez)'

class facebookapiAdmin(admin.ModelAdmin):
    actions = [tokenLargoUsario]
admin.site.register(facebookapi,facebookapiAdmin)