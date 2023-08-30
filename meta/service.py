import requests
from facebooktoken import FacebookTokenRefresher



def tokenAcceslargaduracion(request):
    url = "https://graph.facebook.com/v3.1/503503553031181_1879786498736206?access_token=EAAfs7qqyVycBAHDyl7Q34IXNLwht4ZB2tMz0yukZCiqrZAU5ZA9O5hhVOqV8mehZCPa5SLWpOZAJCZCn5lDZChJe4GVSYq9qYXi2yxAi50Eow28iBZAhjiaVzqPAvrAI5BHgpGYoPXaQGBKrYe1JxDIkUYemytmqX6wvzWZAdOuih6QAJtD63n6TZCeZBTRBOoBqvLIZD"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

def tokenRefresh(request):
    ftr = FacebookTokenRefresher(
    app_id=700797440051611,
    app_secret="485c92c8220b87badbe8f6bb5cd02be7",
    short_access_token="EAAJ9Xx55SZA0BAHmtrLHE3mvthKHW5mbBDXpkW6haI62UBevj8bZB1DWdoGKKtYhevbZBvtyOBHVdC7i3cFmxbO7PaUpjS2yovRO4BWPsNcmRqLzUCcAcU70dkl3WrdrqZAvG1jPWrdcnVJZANKiZCJmqf44vXfNU9kAzA9uqRM0FTzYZBk6P6QYlpQJ2LJiNQZD"
    )

    results = ftr.refresh()

def makemessagepublications(request):
    url = "https://graph.facebook.com/v3.1/107867655737467/feed?message=This%20is%20Test%20message!!!!!!!!!!&access_token=EAANtoxjjAzoBOxZBp0ZB04oyHQ70G9hiPKrWP8Qv6ygxgQmeZBLOz04OxR7qgZC0CC98bqSBCi0pcAuzRIUeFlPl1bahZADxZBBdOnhftGsh9fo1yTiMakbSt6aCCPEHjPLOjpmoZCAH8f6uiLQvocFoUUyZAlD5tphoE1bO1J7eFkPG2LxOzfOl372XdoWhn78ZD"

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)    

#----------Para imagen

def imagenPostamn(request):

        url = "https://graph.facebook.com/v17.0/107867655737467/photos"

        payload = {'access_token': 'EAANtoxjjAzoBOxZBp0ZB04oyHQ70G9hiPKrWP8Qv6ygxgQmeZBLOz04OxR7qgZC0CC98bqSBCi0pcAuzRIUeFlPl1bahZADxZBBdOnhftGsh9fo1yTiMakbSt6aCCPEHjPLOjpmoZCAH8f6uiLQvocFoUUyZAlD5tphoE1bO1J7eFkPG2LxOzfOl372XdoWhn78ZD'}
        files=[
        ('source',('frases-para-facebook-2021.jpg',open('/home/liana/Público/pythonProject/facebook/media/image/frases-para-facebook-2021.jpg','rb'),'image/jpeg'))
        ]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        print(response.text)

def texto_foto(requests):
    url = 'https://graph.facebook.com/964972194759482/feed'
    access_token = 'EAANtoxjjAzoBOxZBp0ZB04oyHQ70G9hiPKrWP8Qv6ygxgQmeZBLOz04OxR7qgZC0CC98bqSBCi0pcAuzRIUeFlPl1bahZADxZBBdOnhftGsh9fo1yTiMakbSt6aCCPEHjPLOjpmoZCAH8f6uiLQvocFoUUyZAlD5tphoE1bO1J7eFkPG2LxOzfOl372XdoWhn78ZD'

# Adjunta la imagen al cuerpo de la solicitud
    files = {'source': open('/home/liana/Público/pythonProject/facebook/media/image/frases-para-facebook-2021.jpg', 'rb')}
#files = {'source': open('ruta_de_la_imagen.jpg', 'rb')}
# Parámetros de la solicitud
    params = {
    'access_token': access_token,
    'message': 'Unavezmas'
    }

# Realiza la solicitud POST para publicar la foto
    response = requests.post(url, params=params, files=files)

# Verifica la respuesta
    if response.status_code == 200:
        print('Foto publicada exitosamente.')
    else:
        print('Hubo un error al publicar la foto.')


def foto_despuesdeTexto(requests):
    url = 'https://graph.facebook.com/{POST_ID}/photos'#{POST_ID} con el ID de la publicación a la que deseas agregar la imagen.
    access_token = 'TU_TOKEN_DE_ACCESO'

# Parámetros de la solicitud
    params = {
        'access_token': access_token,
        'url': 'URL_DE_LA_IMAGEN',
        'published': 'false'
    }
    #También se establece 'published': 'false' para que la imagen no se publique de inmediato, sino que se adjunte a la publicación existente sin cambios adicionales.

# POST request para adjuntar la imagen a la publicación
    response = requests.post(url, params=params)

# Verifica la respuesta
    if response.status_code == 200:
        print('Imagen adjuntada exitosamente.')
    else:
        print('Hubo un error al adjuntar la imagen.')


#Para obtener el id de una publicacion:
import requests

url = 'https://graph.facebook.com/964972194759482/feed'
access_token = 'TU_TOKEN_DE_ACCESO'

# Parámetros de la solicitud
params = {
    'access_token': access_token,
    'message': 'Mi mensaje de prueba'
}

# Realiza la solicitud POST para crear la publicación
response = requests.post(url, params=params)

# Verifica la respuesta
if response.status_code == 200:
    # Obtén el ID de la publicación desde la respuesta JSON
    response_json = response.json()
    post_id = response_json['id']
    print('Publicación creada exitosamente. ID de la publicación:', post_id)
else:
    print('Hubo un error al crear la publicación.')