from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from commerce.models import *

def home(request):
	#produtoLista = Produto.objects.filter(id = 1)
	#produto = produtoLista[0]
	#context = {'produto':produto}
	return render(request, 'commerce/home.html')

def postar(request):
	#produtoLista = Produto.objects.filter(id = 1)
	#produto = produtoLista[0]
	#context = {'produto':produto}
	return render(request, 'commerce/postar.html')
