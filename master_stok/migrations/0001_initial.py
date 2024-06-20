# Generated by Django 5.0.6 on 2024-06-20 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterStock',
            fields=[
                ('kode_barang', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_barang', models.CharField(max_length=255)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]