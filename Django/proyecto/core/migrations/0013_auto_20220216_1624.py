# Generated by Django 3.2.10 on 2022-02-16 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_article_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='article',
            name='descripcionAll',
        ),
        migrations.RemoveField(
            model_name='article',
            name='objetivoGeneral',
        ),
        migrations.RemoveField(
            model_name='article',
            name='synonyms',
        ),
    ]
