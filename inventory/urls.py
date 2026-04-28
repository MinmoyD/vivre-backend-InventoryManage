from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, InventoryLogViewSet, add_stock, remove_stock

router = DefaultRouter()
router.register(r'products',ProductViewSet)
router.register(r'logs', InventoryLogViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('inventory/add/', add_stock, name='add_stock'),
    path('inventory/remove/', remove_stock, name='remove_stock'),
]