from django.contrib import admin

from Laporan.models import LaporanKeuangan, Pembayaran
from Orderan.models import GambarOrderan, HistoriOrderan, Orderan
from Pengguna.models import Admin, Pelanggan
from Pengiriman.models import Pengiriman

# Register your models here.
admin.site.register(Admin)
admin.site.register(Pelanggan)
admin.site.register(Orderan)
admin.site.register(GambarOrderan)
admin.site.register(HistoriOrderan)
admin.site.register(LaporanKeuangan)
admin.site.register(Pengiriman)
admin.site.register(Pembayaran)