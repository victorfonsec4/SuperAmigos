from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from commerce.models import *
import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
import json

class ProdutoForm(forms.Form):
	nome = forms.CharField(max_length=100)
	preco = forms.IntegerField()
	descricao = forms.CharField()
	urlFoto = forms.CharField()

class DeleteForm(forms.Form):
	id = forms.IntegerField()


@csrf_exempt
def home(request):
	lista = []
	if request.method == 'POST':
		listaAmigos = request.GET.get('response')
		#listaAmigos = get_friends(access_token).json()['friends']['data']
		#listaNome = []
		for amigo in listaAmigos:
			lista.extend(Produto.objects.filter(usuario = amigo['id']))
			#listaNome.extend(amigo['name'])
	else:
		lista.extend(Produto.objects.filter(usuario = 1))
	#listaFinal = (lista, listaNome)
	#context = {'lista':listaFinal}
	context = {'lista' : lista}
	return render(request, 'commerce/home.html', context)

@csrf_exempt
def postar(request):
	#produtoLista = Produto.objects.filter(id = 1)
	#produto = produtoLista[0]
	#context = {'produto':produto}
	return render(request, 'commerce/postar.html')

@csrf_exempt
def login(request):
	return render(request, 'commerce/login.html', context)
@csrf_exempt	

def get_friends(access_token):
	r = requests.get('https://graph.facebook.com/me?fields=id,friends&access_token=' + access_token)
	return r

@csrf_exempt	
def friendlist (request):
	access_token = request.GET.get('access_token')
	r = get_friends(access_token)
	context = {'access_token' : access_token, 'text' : r.text}
	return render(request, 'commerce/friendlist.html', context)
	
@csrf_exempt
def adicionar(request):
	produtoForm = ProdutoForm(request.POST)
	nome = produtoForm.data['nome']
	preco = produtoForm.data['preco']
	descricao = produtoForm.data['descricao']
	urlFoto = produtoForm.data['urlFoto']
	produtoAdd = Produto(nome=nome,preco=preco,descricao=descricao,usuario=1,urlFoto=urlFoto)
	produtoAdd.save()
	return HttpResponseRedirect('/home')

@csrf_exempt	
def deletar (request):
	lista = []
	lista = Produto.objects.filter(usuario = 1)
	context = {'lista':lista}
	return render(request, 'commerce/deletar.html', context)

@csrf_exempt	
def deletando (request):
	deleteForm = DeleteForm(request.POST)
	deleteid = deleteForm.data['id']
	Produto.objects.filter(id=deleteid).delete()
	return HttpResponseRedirect('/deletar')

@csrf_exempt
def login2(request):
	return render(request, 'commerce/login2.html')

@csrf_exempt
def getdata(request):
	userId = request.POST['id']
	nome = request.POST['name']
	request.POST.pop('id', none)
	request.POST.pop('name', none)
	friendList = request.POST
	#usuario = Usuario(userid = userId, nome = nome, json = friendList)
	#usuario.save()
	return render(request, 'commerce/home.html')

