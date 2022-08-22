from multiprocessing import context
from django.template import Context, Template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import MySQLdb

# Create your views here.
def index(request):
    return render(request,'inicio/index.html')
@login_required
def home(request):
    db = MySQLdb.connect(user='sistemas', db='ricsa', passwd='Aca$', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT count(*) FROM usuarios')
    usuarios =  cursor.fetchall
    print(usuarios)
    cursor.execute('SELECT count(*) FROM login')
    login = cursor.fetchall
    db.close()
    c = Context({'usuarios':usuarios, 'login':login})
    
    return render(request,'plantilla/index.html', {'context': c})
    
def salir(request):
    logout(request)
    return redirect('/home')
