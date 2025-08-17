from django.contrib import admin
from .models import Barang, Transaksi
from .models import Supplier

@admin.register(Barang)
class BarangAdmin(admin.ModelAdmin):
    list_display = ('kode_barang' if hasattr(Barang, 'kode_barang') else 'code', 'name' if hasattr(Barang,'name') else 'nama_barang', 'status_barang', 'qty_total')
    search_fields = ('kode_barang', 'name', 'nama_barang')
    list_filter = ('status_barang',)

@admin.register(Transaksi)
class TransaksiAdmin(admin.ModelAdmin):
    list_display = ('jenis', 'item', 'qty', 'status_barang', 'created_at', 'created_by')
    list_filter = ('jenis', 'status_barang', 'created_at')
    search_fields = ('item__kode_barang', 'item__name', 'item__nama_barang')

    from django.contrib import admin

@admin.register(Supplier) 
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("nama_supplier", "telepon")   # kolom yg tampil
    search_fields = ("nama_supplier", "telepon") # bisa search
