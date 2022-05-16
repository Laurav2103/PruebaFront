from pyexpat import model
from django import forms
from .models import cliente


class ArticleForm(forms.ModelForm):
    class Meta:
        model = cliente
       # fields = '_all_'
        fields = ('EstadoERP', 'TipoDocumento',
                  'NombreCliente', 'NoLineas', 'FechaPedido', 'Pedido', 'EstadoSiesa', 'PedidoSiesa')
