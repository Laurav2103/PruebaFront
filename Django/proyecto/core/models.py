from email.policy import default
from enum import Flag
from multiprocessing.sharedctypes import Value
from os import link
from xml.dom.expatbuilder import FilterVisibilityController
from django import urls
from django.db import models
from django.http import HttpResponse
from import_export import resources
from sqlalchemy import true
from collections import Iterable
import spacy
import nltk
from nltk import SnowballStemmer
import unicodedata

# Create your models here.


class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    EstadoERP = models.CharField(max_length=350)
    TipoDocumento = models.CharField(max_length=350)
    NombreCliente = models.CharField(max_length=350)
    NoLineas = models.CharField(
        max_length=350, verbose_name="No de lineas")
    FechaPedido = models.CharField(
        max_length=550, verbose_name="Fecha")
    Pedido = models.CharField(max_length=550)
    EstadoSiesa = models.CharField(max_length=550)
    PedidoSiesa = models.CharField(max_length=550)

    def __str__(self):
        return self.NombreCliente

    def get_model_fields(self):
        return self._meta.fields

    """def __iter__(self):
        convs = self.synonyms
        list(convs)
        return iter(convs)"""

    def save(self, *args, **kwargs):
        print('save() is called.')
        super(cliente, self).save(*args, **kwargs)
        """articles = article.objects.all()
        p = article.save()
        print(p.id)
        id = p.id
        article.updateFields(id)"""
