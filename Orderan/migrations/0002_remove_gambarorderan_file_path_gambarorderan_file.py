# Generated by Django 5.1.1 on 2024-10-30 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orderan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gambarorderan',
            name='file_path',
        ),
        migrations.AddField(
            model_name='gambarorderan',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
