from django.db import models

from Pengguna.models import Pelanggan

# Create your models here.
class Orderan(models.Model):
    ID_Pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    Tanggal_Order = models.DateField(null=False)
    Jenis_Orderan = models.CharField(max_length=50, null=True)
    Ukuran_Orderan = models.CharField(max_length=50, null=True)
    Jumlah_orderan = models.IntegerField(null=True)
    Harga_Total = models.DecimalField(max_digits=10, decimal_places=2)
    Status_Orderan = models.CharField(max_length=50, default="Belum Diproses")

    def __str__(self):
        return f"Order #{self.id} by {self.ID_Pelanggan.Nama_pelanggan}"

class GambarOrderan(models.Model):
    ID_Orderan = models.ForeignKey(Orderan, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    Deskripsi = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'GambarOrderan {self.ID_Orderan}'

class HistoriOrderan(models.Model):
    ID_Orderan = models.ForeignKey(Orderan, on_delete=models.CASCADE)
    Tanggal_Perubahan = models.DateTimeField(auto_now_add=True)
    Status_Baru = models.CharField(max_length=50)
    Catatan = models.TextField(null=True, blank=True)

    def _str_(self):
        return f"Histori for Order #{self.ID_Orderan.id} on {self.Tanggal_Perubahan}"