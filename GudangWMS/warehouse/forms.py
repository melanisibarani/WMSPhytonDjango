from django import forms

class BarangMasukForm(forms.Form):
    kode_barang = forms.CharField(max_length=50, label="Kode Barang (scan QR)")
    qty = forms.IntegerField(min_value=1, label="Qty")

class BarangKeluarForm(forms.Form):
    kode_barang = forms.CharField(max_length=50, label="Kode Barang (scan QR)")
    qty = forms.IntegerField(min_value=1, label="Qty")