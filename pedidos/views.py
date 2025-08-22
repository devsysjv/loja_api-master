# views.py
from django.shortcuts import render
from django.http import HttpResponse

def lista_produtos(request):
    return HttpResponse("listagem de produtos")

