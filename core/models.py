
from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPES = (
    ('admin', 'Administrador'),
    ('funcionario', 'Funcionário'),
    ('revendedor', 'Revendedor'),
    ('subdistribuidor', 'Subdistribuidor'),
    ('sdg', 'Equipe SDG'),
)

OPERADORAS = (
    ('unitel', 'Unitel'),
    ('africell', 'Africell'),
)

TIPOS_RECARGA = (
    ('fisica', 'Física'),
    ('digital', 'Digital'),
)

class User(AbstractUser):
    tipo = models.CharField(max_length=20, choices=USER_TYPES)

class Revendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)

class PontoVenda(models.Model):
    revendedor = models.ForeignKey(Revendedor, on_delete=models.CASCADE)
    localizacao = models.CharField(max_length=255)
    gps = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)

class Inventario(models.Model):
    operadora = models.CharField(max_length=20, choices=OPERADORAS)
    tipo = models.CharField(max_length=20, choices=TIPOS_RECARGA)
    saldo = models.DecimalField(max_digits=12, decimal_places=2)

class Venda(models.Model):
    revendedor = models.ForeignKey(Revendedor, on_delete=models.CASCADE)
    operadora = models.CharField(max_length=20, choices=OPERADORAS)
    tipo = models.CharField(max_length=20, choices=TIPOS_RECARGA)
    numero_telefone = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

class Comissao(models.Model):
    venda = models.OneToOneField(Venda, on_delete=models.CASCADE)
    percentual = models.DecimalField(max_digits=5, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Bonus(models.Model):
    revendedor = models.ForeignKey(Revendedor, on_delete=models.CASCADE)
    valor_compra = models.DecimalField(max_digits=12, decimal_places=2)
    valor_bonus = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

class FluxoCaixa(models.Model):
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
