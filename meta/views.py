from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
def home(request):
    return render(request, 'home.html')
def facebook_data_view(request):
    # Obtener el token de acceso del usuario, por ejemplo, a través de una sesión o base de datos.
    token = 'EABnyao4k9EoBO9OMD09deegFjUDji24ZAA34HuuYxDZBaagp37Fg8IoZCZBsSNQv7QUMhrZCQTW3KaRTs1S8Bvr87P8TGC086koDnQII1wxZBnafXJqPfpZAHUZAE4BsUlZA9yk45HgNZCrwPE5srtNwfWILu9hcUyOXy1ZAbkZA1rXp3nZAUbIU3bsndduq2Q59V0CClWQZDZD'
    url = 'https://graph.facebook.com/v12.0/me?metadata=1'
    response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
    data = response.json()
    return render(request, 'facebook_data.html', {'data': data})

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
