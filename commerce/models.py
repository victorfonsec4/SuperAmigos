from django.db import models

class Produto(models.Model):
	nome = models.CharField(max_length=50)
	preco = models.IntegerField(default = 0)
	descricao = models.TextField()
	usuario = models.CharField(max_length = 50)
	urlFoto = models.TextField()
	def __unicode__(self):
		return self.nome
class Usuario(models.Model):
	userid = models.TextField()
	nome = models.TextField()
	json = models.TextField()
	def __unicode__(self):
		return self.nome
