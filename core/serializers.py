from rest_framework import serializers
from .models import (
    User, Revendedor, PontoVenda, Inventario,
    Venda, Comissao, Bonus, FluxoCaixa
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RevendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revendedor
        fields = '__all__'

class PontoVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontoVenda
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'

class ComissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comissao
        fields = '__all__'

class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = '__all__'

class FluxoCaixaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FluxoCaixa
        fields = '__all__'