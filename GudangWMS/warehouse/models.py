from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User
STATUS_CHOICES = [
    ('aktif', 'Aktif'),
    ('nonaktif', 'Non Aktif'),
]

DELIVERY_CHOICES = [
    ('delivery', 'Delivery'),
    ('non_delivery', 'Non Delivery'),
]

class Barang(models.Model):
    kode_barang = models.CharField(max_length=20, unique=True)
    nama_barang = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='foto_barang/', blank=True, null=True)
    status_barang = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aktif')
    status_pengiriman = models.CharField(max_length=15, choices=DELIVERY_CHOICES, default='delivery')
    qty_total = models.IntegerField(default=0)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(self.kode_barang)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        file_name = f'{self.kode_barang}_qr.png'
        self.qr_code.save(file_name, File(buffer), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.kode_barang} - {self.nama_barang}"
class Transaksi(models.Model):
    IN = 'IN'
    OUT = 'OUT'
    JENIS_CHOICES = [
        (IN, 'Barang Masuk'),
        (OUT, 'Barang Keluar'),
    ]

    item = models.ForeignKey('Barang', on_delete=models.PROTECT, related_name='transactions')
    jenis = models.CharField(max_length=3, choices=JENIS_CHOICES)
    qty = models.PositiveIntegerField()
    status_barang = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aktif')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_jenis_display()} - {self.item.code if hasattr(self.item,'code') else self.item.kode_barang} - {self.qty}"


class Supplier(models.Model):
    nama_supplier = models.CharField(max_length=200)
    alamat = models.TextField(blank=True, null=True)
    telepon = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nama_supplier
