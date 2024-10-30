# Generated by Django 5.1.1 on 2024-09-26 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Admin', models.CharField(max_length=50, null=True)),
                ('Password', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_pelanggan', models.CharField(max_length=100, null=True)),
                ('Email', models.CharField(max_length=50, null=True)),
                ('No_Telepon', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]