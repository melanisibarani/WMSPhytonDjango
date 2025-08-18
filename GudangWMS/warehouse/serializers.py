
from rest_framework import serializers
from .models import Barang

class BarangSerializer(serializers.ModelSerializer):
    foto_url = serializers.SerializerMethodField(read_only=True)
    qr_code_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Barang
        fields = [
            "id", "kode_barang", "nama_barang", "deskripsi",
            "foto", "foto_url",
            "status_barang", "status_pengiriman",
            "qty_total",
            "qr_code_url",
        ]
        read_only_fields = ["qr_code_url"]  # QR dibuat otomatis di model.save()

    def get_foto_url(self, obj):
        request = self.context.get("request")
        if obj.foto and request:
            return request.build_absolute_uri(obj.foto.url)
        return None

    def get_qr_code_url(self, obj):
        request = self.context.get("request")
        if obj.qr_code and request:
            return request.build_absolute_uri(obj.qr_code.url)
        return None

    def validate_qty_total(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("qty_total tidak boleh negatif.")
        return value
