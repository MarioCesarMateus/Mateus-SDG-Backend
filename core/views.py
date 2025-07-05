from rest_framework import viewsets
from .models import (
    User, Revendedor, PontoVenda, Inventario,
    Venda, Comissao, Bonus, FluxoCaixa
)
from .serializers import (
    UserSerializer, RevendedorSerializer, PontoVendaSerializer,
    InventarioSerializer, VendaSerializer, ComissaoSerializer,
    BonusSerializer, FluxoCaixaSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RevendedorViewSet(viewsets.ModelViewSet):
    queryset = Revendedor.objects.all()
    serializer_class = RevendedorSerializer

class PontoVendaViewSet(viewsets.ModelViewSet):
    queryset = PontoVenda.objects.all()
    serializer_class = PontoVendaSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class ComissaoViewSet(viewsets.ModelViewSet):
    queryset = Comissao.objects.all()
    serializer_class = ComissaoSerializer

class BonusViewSet(viewsets.ModelViewSet):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

class FluxoCaixaViewSet(viewsets.ModelViewSet):
    queryset = FluxoCaixa.objects.all()
    serializer_class = FluxoCaixaSerializer