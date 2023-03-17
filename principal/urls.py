from http import client
from django import views
from django.urls import path, include
from django.views.generic import *
from .views import *
urlpatterns = [
    path('home',home,name='home'),
    path('',index,name='index'),
    path('clientes',login_required(ClientesListView.as_view()),name='clientes'),
    path('update/<int:pk>',login_required(actualizarcliente.as_view()),name='update'),
    path('updatepaquete/<int:pk>',login_required(actualizarpaquete.as_view()),name='updatepaquete'),
    path('updatecampaña/<int:pk>',login_required(actualizarcampaña.as_view()),name='updatecampaña'),
    path('campañas',login_required(CampañasListView.as_view()),name='campañas'),
    path('paquetes',login_required(PaquetesListView.as_view()),name='paquetes'),
    path('monitoreo',login_required(monitoreo),name='monitoreo'),
    path('usuarios',login_required(UsuariosListView.as_view()),name='usuarios'),
    path('views',login_required(ViewsListView.as_view()),name='views'),
    path('verc/<int:pk>',mostrarcliente,name='verc'),
    path('deletec/<int:pk>',deletecliente,name='deletec'),
    path('deletep/<int:pk>',deletepaquete,name='deletep'),
    path('deletecam/<int:pk>',deletecampaña,name='deletecam'),
    path('salir',salir,name='salir')
]