from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Barang
from .serializers import BarangSerializer

class BarangViewSet(viewsets.ModelViewSet):
    queryset = Barang.objects.all().order_by("kode_barang")
    serializer_class = BarangSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    # filter / search / order
    filterset_fields = ["status_barang", "status_pengiriman"]
    search_fields = ["kode_barang", "nama_barang", "deskripsi"]
    ordering_fields = ["kode_barang", "nama_barang", "qty_total", "id"]
