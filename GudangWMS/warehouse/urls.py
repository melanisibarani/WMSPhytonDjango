from django.urls import path
from . import views

urlpatterns = [
    path('in/', views.barang_masuk, name='barang_masuk'),
    path('out/', views.barang_keluar, name='barang_keluar'),
    path('out/<int:pk>/print/', views.print_keluar, name='print_keluar'),
    path('stock/', views.stok_list, name='stok_list'),
    path('stock/<int:item_id>/card/', views.kartu_stok, name='kartu_stok'),

     # >>> REPORTS <<<
    path('reports/transaksi/', views.report_transaksi, name='report_transaksi'),
    path('reports/transaksi/export/pdf/', views.export_transaksi_pdf, name='export_transaksi_pdf'),
    path('reports/transaksi/export/xlsx/', views.export_transaksi_xlsx, name='export_transaksi_xlsx'),

    path('reports/stok/', views.report_stok, name='report_stok'),
    path('reports/stok/export/pdf/', views.export_stok_pdf, name='export_stok_pdf'),
    path('reports/stok/export/xlsx/', views.export_stok_xlsx, name='export_stok_xlsx'),
    path("barang_masuk/", views.barang_masuk, name="barang_masuk"),
    path("barang-masuk/upload-qr/", views.upload_qr, name="upload_qr"),

]

