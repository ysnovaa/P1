from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Bienvenido a mi pagina de inicio papu</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name':'Yoban Nova '})