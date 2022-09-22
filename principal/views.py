from asyncio import QueueEmpty
from msilib.schema import ListView
from multiprocessing import context
from datetime import datetime, timedelta
from tkinter.tix import Form

from django.template import Context, Template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from json import dumps 
import MySQLdb
from .forms import *
from .models import clientes as Clientes
from django.views.generic import ListView

# Create your views here.
def index(request):
    return render(request,'inicio/index.html')
@login_required
def home(request):
    fecha7 = datetime.today()-timedelta(days=7) 
    fecha7 = fecha7.strftime('%Y-%m-%d')
    fecha6 = datetime.today()-timedelta(days=6)
    fecha6 = fecha6.strftime('%Y-%m-%d')
    fecha5 = datetime.today()-timedelta(days=5)
    fecha5 = fecha5.strftime('%Y-%m-%d')
    fecha4 = datetime.today()-timedelta(days=4)
    fecha4 = fecha4.strftime('%Y-%m-%d')
    fecha3 = datetime.today()-timedelta(days=3)
    fecha3 = fecha3.strftime('%Y-%m-%d')
    fecha2 = datetime.today()-timedelta(days=2)
    fecha2 = fecha2.strftime('%Y-%m-%d')
    fecha1 = datetime.today()-timedelta(days=1)
    fecha1 = fecha1.strftime('%Y-%m-%d')
   
    db = MySQLdb.connect(user='sistemas', db='ricsa', passwd='Aca$', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT count(*) FROM usuarios')
    usuarios =  cursor.fetchone()[0]
    cursor.execute('SELECT count(*) FROM login')
    login = cursor.fetchone()[0]
    cursor.execute('SELECT count(distinct cliente) from videos')
    clientes = cursor.fetchone()[0]
    cursor.execute("SELECT count(*) from login where fecha BETWEEN  '%s'and '%s'" % (fecha7+' 00:00:00',fecha7+' 23:59:59'))
    views7 = cursor.fetchone()[0]
    cursor.execute("SELECT count(*) from login where fecha BETWEEN  '%s'and '%s'" % (fecha6+' 00:00:00',fecha6+' 23:59:59'))
    views6 = cursor.fetchone()[0]
    cursor.execute("SELECT count(*) from login where fecha BETWEEN  '%s'and '%s'" % (fecha5+' 00:00:00',fecha5+' 23:59:59'))
    views5 = cursor.fetchone()[0]
    cursor.execute("SELECT count(*) from login where fecha BETWEEN  '%s'and '%s'" % (fecha4+' 00:00:00',fecha4+' 23:59:59'))
    views4 = cursor.fetchone()[0]
    cursor.execute("SELECT count(*) from login where fecha BETWEEN  '%s'and '%s'" % (fecha3+' 00:00:00',fecha3+' 23:59:59'))
    views3 = cursor.fetchone()[0]
    cursor.execute("SELECT count(*) from login where fecha BETWEEN  '%s'and '%s'" % (fecha2+' 00:00:00',fecha2+' 23:59:59'))
    views2 = cursor.fetchone()[0]
    cursor.execute("SELECT count(*) from login where fecha BETWEEN  '%s'and '%s'" % (fecha1+' 00:00:00',fecha1+' 23:59:59'))
    views1 = cursor.fetchone()[0]
    db.close()
    c = Context({'usuarios':usuarios, 'login':login, 'clientes':clientes, 'views7':views7,'views6':views6,
    'views5':views5,'views4':views4,'views3':views3,'views2':views2,'views1':views1})
    return render(request,'plantilla/index.html', {'context': c})

class ClientesListView(ListView):
    context = {}

    def get(self,request):
        form = ClientesForm()
        self.context['form'] = form
        self.context['Clientes'] = Clientes.objects.all()
        return render(request,'plantilla/clientes.html',self.context)
    def post(self,request):
        
        form = ClientesForm(request.POST)
        if form.is_valid():
            print('valido')
            form.save()
        self.context['form'] = form
        self.context['Clientes'] = Clientes.objects.all()
        return render(request, 'plantilla/clientes.html', self.context)
def campañas(request):

    data ={
    'form':CampañasForm()
    }
    if request.method=='POST':
            addcampaña=CampañasForm(data=request.POST)
            if addcampaña.is_valid():
                addcampaña.save()
                addcampaña = CampañasForm()
                data["mensaje"]="campaña guardado"
                print('valido')
                return redirect('plantilla/campañas')
            else:
                print('invalido')
                data["form"] = addcampaña
    return render(request,'plantilla/campañas.html',data)
def paquetes(request):
    data ={
    'form':PaquetesForm()
    }
    if request.method=='POST':
            addpaquetes=PaquetesForm(data=request.POST)
            if addpaquetes.is_valid():
                addpaquetes.save()
                addpaquetes = PaquetesForm()
                data["mensaje"]="Paquete guardado"
                print('valido')
                return redirect('plantilla/paquete')
            else:
                print('invalido')
                data["form"] = addpaquetes
    return render(request,'plantilla/paquete.html',data)

def salir(request):
    logout(request)
    return redirect('/home')
