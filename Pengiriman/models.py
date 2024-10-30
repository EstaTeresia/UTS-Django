from django.db import models

from Orderan.models import Orderan

# Create your models here.
class Pengiriman(models.Model):
    ID_Orderan = models.ForeignKey(Orderan, on_delete=models.CASCADE)
    Tanggal_Kirim = models.DateField(null=False)
    Status_Pengiriman = models.CharField(max_length=50, default="Sedang Diproses")
    Alamat_Pengiriman = models.TextField()