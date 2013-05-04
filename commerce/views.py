from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from commerce.models import *

def home(request):
	#produtoLista = Produto.objects.filter(id = 1)
	#produto = produtoLista[0]
	#context = {'produto':produto}
	return render(request, 'commerce/home.html', context)

def login(request):
	code = request.GET.get('code')
	context = {'code' : code}
	return render(request, 'commerce/login.html', context)
	
def friendlist (request):
	access_token = request.GET.get('access_token')
	context = {'access_token' : access_token}
	return render(request, 'commerce/friendlist.html', context)