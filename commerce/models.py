from django.db import models

class Produto(models.Model):
	nome = models.CharField(max_length=50)
	preco = models.IntegerField(default = 0)
	descricao = models.CharField(max_length=255)

	def __unicode__(self):
		return self.nome
