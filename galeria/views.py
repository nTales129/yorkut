from django.shortcuts import render


def  index(request):
    return render(request, 'galeria/index.html')

def cadastro(request):
    return render(request, 'galeria/cadastro.html')
    

# Create your views here.
