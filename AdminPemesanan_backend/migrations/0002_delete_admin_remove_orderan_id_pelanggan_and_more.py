# Generated by Django 5.1.1 on 2024-09-26 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPemesanan_backend', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.RemoveField(
            model_name='orderan',
            name='ID_Pelanggan',
        ),
        migrations.RemoveField(
            model_name='pembayaran',
            name='ID_Orderan',
        ),
        migrations.DeleteModel(
            name='Pelanggan',
        ),
        migrations.DeleteModel(
            name='Orderan',
        ),
        migrations.DeleteModel(
            name='Pembayaran',
        ),
    ]