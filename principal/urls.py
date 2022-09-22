from http import client
from django.urls import path, include
from django.views.generic import *
from .views import *
urlpatterns = [
    path('home',home,name='home'),
    path('',index,name='index'),
    path('clientes',ClientesListView.as_view(),name='clientes'),
    path('campañas',campañas,name='campañas'),
    path('paquetes',paquetes,name='paquetes'),
    path('salir',salir,name='salir')
]