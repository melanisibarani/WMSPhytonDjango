from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import BarangViewSet

router = DefaultRouter()
router.register(r'barang', BarangViewSet, basename='barang')

urlpatterns = [
    path('', include(router.urls)),
]
