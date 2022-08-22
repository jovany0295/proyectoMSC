from django.urls import path, include
from .views import index, salir,home

urlpatterns = [
    path('home',home,name='home'),
    path('',index,name='index'),
    path('salir',salir,name='salir')
]