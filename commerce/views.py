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

def login(request):
	return render(request, 'commerce/login.html')
	
def friendlist (request):
	access_token = request.GET.get('access_token')
	context = {'access_token':access_token}
	return render(request, 'commerce/friendlist.html', context)
