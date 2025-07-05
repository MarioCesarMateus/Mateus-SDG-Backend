
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, RevendedorViewSet, PontoVendaViewSet,
    InventarioViewSet, VendaViewSet, ComissaoViewSet,
    BonusViewSet, FluxoCaixaViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'revendedores', RevendedorViewSet)
router.register(r'pontos-venda', PontoVendaViewSet)
router.register(r'inventario', InventarioViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'comissoes', ComissaoViewSet)
router.register(r'bonus', BonusViewSet)
router.register(r'fluxo-caixa', FluxoCaixaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
