# Generated by Django 3.2.10 on 2022-05-16 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20220516_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='estadoERP',
            new_name='EstadoERP',
        ),
    ]
