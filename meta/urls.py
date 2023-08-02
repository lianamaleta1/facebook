from django.urls import path,include
from . import views

from .views import FacebookLogin

urlpatterns = [
    path('accounts/login/',views.autenticar,name="autenticar"),
    path('', views.inicio, name='inicio'),
    path('logout/',views.logoutView, name='logout'),
    path('facebook_posts/', views.facebook_posts, name='facebook_posts'),
    path('info/', views.facebook_data_view, name='facebook_data_view'),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='rest_login_facebook'),
    path('facebook-login/', FacebookLogin.as_view(), name='facebook_login'),
    path('home/',views.home, name='home'),

]