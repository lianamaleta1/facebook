from django.urls import path,include
from . import views


urlpatterns = [
    path('info/',views.facebook_data_view,name="facebook_data_view"),
]