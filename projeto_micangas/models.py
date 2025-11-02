from django.db import models

class Micanga(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    cor = models.CharField(max_length=50)
    estoque = models.PositiveIntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='micangas/', blank=True, null=True)


    def __str__(self):
        return self.nome
