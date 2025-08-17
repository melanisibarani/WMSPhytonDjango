from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.db.models import F
from .models import Transaksi, Barang

@receiver(pre_save, sender=Transaksi)
def update_stock_on_save(sender, instance, **kwargs):
    """
    Hitung delta stok ketika transaksi dibuat/diupdate.
    """
    # transaksi lama (kalau update)
    old_delta = 0
    if instance.pk:
        prev = Transaksi.objects.get(pk=instance.pk)
        old_delta = prev.qty if prev.jenis == Transaksi.IN else -prev.qty

    # transaksi baru
    new_delta = instance.qty if instance.jenis == Transaksi.IN else -instance.qty

    delta = new_delta - old_delta
    if delta != 0:
        Barang.objects.filter(pk=instance.item_id).update(qty_total=F('qty_total') + delta)

@receiver(post_delete, sender=Transaksi)
def update_stock_on_delete(sender, instance, **kwargs):
    """
    Balikkan efek stok jika transaksi dihapus.
    """
    delta = -instance.qty if instance.jenis == Transaksi.IN else instance.qty
    Barang.objects.filter(pk=instance.item_id).update(qty_total=F('qty_total') + delta)