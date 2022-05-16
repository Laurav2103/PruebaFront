# Generated by Django 3.2.10 on 2022-05-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20220217_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estadoERP', models.CharField(max_length=350)),
                ('TipoDocumento', models.CharField(max_length=350)),
                ('NombreCliente', models.CharField(max_length=350)),
                ('NoLineas', models.CharField(max_length=350, verbose_name='Nombre del estudio')),
                ('FechaPedido', models.CharField(max_length=550, verbose_name='Catalogación')),
                ('Pedido', models.CharField(max_length=550)),
                ('EstadoSiesa', models.CharField(max_length=550)),
                ('PedidoSiesa', models.CharField(max_length=550)),
            ],
        ),
        migrations.DeleteModel(
            name='article',
        ),
    ]