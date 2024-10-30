from django.db import models

from Orderan.models import Orderan

# Create your models here.
class LaporanKeuangan(models.Model):
    Tanggal = models.DateField(null=False)
    Total_Pemasukan = models.DecimalField(max_digits=10, decimal_places=2)
    Total_Pengeluaran = models.DecimalField(max_digits=10, decimal_places=2)
    Laba_Bersih = models.DecimalField(max_digits=10, decimal_places=2)

class Pembayaran(models.Model):
    ID_Orderan = models.ForeignKey(Orderan, on_delete=models.CASCADE)
    Metode_Pembayaran = models.CharField(max_length=50, null=True)
    Status_Pembayaran = models.CharField(max_length=50, null=True)
    Tanggal_Pembayran = models.DateField(null=False)