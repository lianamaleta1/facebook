from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from .models import *



#crear una publicacion desde el panel de administracion, crear un dev con el link q te permita crear la publicacion con los campos necesarios con grap api en una pagina y despues ver como grap api me deja compartirlo hacer hoy OJOOOOOOOOOOOOOO
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
def home(request):
    return render(request, 'home.html')

def autenticar(request):
    return render(request, 'index.html')


def inicio(request):
    if request.user.is_authenticated:
       return redirect('admin:index')
    return render(request,'index.html')

def logoutView(request):
   logout(request)
   return redirect('inicio')

from django.shortcuts import render

def facebook_posts(request):
    # Obtener información del usuario y sus publicaciones de Facebook
    user_info = ...
    user_posts = ...

    context = {
        'user_info': user_info,
        'user_posts': user_posts,
    }

    return render(request, 'facebook_posts.html', context)


def obtener_token_acceso(app_id, app_secret, codigo):
    url = 'https://graph.facebook.com/v12.0/oauth/access_token'
    params = {
        'client_id': app_id,
        'client_secret': app_secret,
        'code': codigo,
        'redirect_uri': 'TU_REDIRECT_URI'  # Reemplaza con la URL de redireccionamiento configurada en tu aplicación
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['access_token']
        return access_token
    else:
        print('Error al obtener el token de acceso:', response.json())
        return None

# Ejemplo de uso
app_id = 'TU_APP_ID'
app_secret = 'TU_APP_SECRET'
codigo_autorizacion = 'CODIGO_DE_AUTORIZACION'

token_acceso = obtener_token_acceso(app_id, app_secret, codigo_autorizacion)
if token_acceso:
    print('Token de acceso obtenido:', token_acceso)

#Obtener un token de acceso de larga duracion para usuario 
def tokenLargoUsario(request):
    
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

# Imprime el token de acceso de larga duración
    print(long_token)

    #-------------Crear una publicacion con tgexto y fotos----------------
    import requests

def createPublicacion(request,id_publicacion):
    post=publicacion.objects.get(pk=id_publicacion)
    imagenes=imagen.objects.filter(publicacion=id_publicacion)

    url = "https://graph.facebook.com/v17.0/107867655737467/photos"
    access_token = "EAANtoxjjAzoBOxZBp0ZB04oyHQ70G9hiPKrWP8Qv6ygxgQmeZBLOz04OxR7qgZC0CC98bqSBCi0pcAuzRIUeFlPl1bahZADxZBBdOnhftGsh9fo1yTiMakbSt6aCCPEHjPLOjpmoZCAH8f6uiLQvocFoUUyZAlD5tphoE1bO1J7eFkPG2LxOzfOl372XdoWhn78ZD"
    message = post.texto

    """Para una sola imagen
    image_path = imagenes.imagen

    files = {
        'source': open(image_path, 'rb')
    }
    """
    files = []

    # Adjuntar cada imagen al formulario de solicitud o sea para varias imagenes    
    for imagen_obj in imagenes:
        files.append(('source', open(imagen_obj.imagen.path, 'rb')))

    data = {
        'access_token': access_token,
        'message': message
    }

    response = requests.post(url, files=files, data=data)

    print(response.text)

def principal(request,id_publicacion):
    post = publicacion.objects.get(pk=id_publicacion)
    imagenes = imagen.objects.filter(publicacion=id_publicacion)

    context = {
        'publicacion': post,
        'imagenes': imagenes,
    }

    createPublicacion(request, id_publicacion)

    return render(request, 'facebook_posts.html',context)    

#--------------Creando publicacion en GRUPOS-----------------
def publicarGrupo(request):
    
    url = 'https://graph.facebook.com/v10.0/835141254719072/photos'
    access_token = 'EAANtoxjjAzoBO3vR7fB8Jdy2eFpBSqMmX5jS6T7h9ZAZCVdHfBaZCFdlZAMzjt0Ou9F78ocOedIGPIdEqdSJ7WHTzCCzgePbctTbAmyituZAyrVwp7YWmVO2Fcbebm8IKUfXaxmlZBcTbL6S4RTDj6uyuxLPrRZCd6n94QLD6BKwZBhXkUZCIHGeDkK0F'
    message = "Este es el texto de la publicación"
    image_path = '/home/liana/Público/pythonProject/facebook/media/image/frases-para-facebook-2021.jpg'

    headers = {'Authorization': f'Bearer {access_token}'}

    files = {'source': open(image_path, 'rb')}
    data = {'message': message}

    response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code == 200:
        print('La imagen se cargó exitosamente.')
    else:
        print('Error al cargar la imagen:', response.json())