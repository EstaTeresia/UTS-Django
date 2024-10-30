from django.db import models

# Create your models here.
class Admin(models.Model):
    Nama_Admin = models.CharField(max_length=50, null=True)
    Password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.Nama_Admin

class Pelanggan(models.Model):
    Nama_pelanggan = models.CharField(max_length=100, null=True)
    Email = models.CharField(max_length=50, null=True)
    No_Telepon = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.Nama_pelanggan