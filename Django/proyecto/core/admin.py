from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import cliente


# Register your models here.

class articleResourse(resources.ModelResource):
    class Meta:
        model = cliente
       # exclude = ('id')


class articleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['NombreCliente', 'estadoERP']
    # list_display = ['categoria', 'segmento', 'producto' , 'nombreArticulo', 'descripcion', 'descripcionAll', 'fechaRecibido', 'NombreArchivoPDF', 'fotoNombreImagen', 'fechaPublicacion', 'estado', 'autor', 'enlace',
    #  'sabiasQue', 'objetivoGeneral', 'objetivoEspecifico', 'tipoEstudio', 'metodologia', 'tamañoMuestra', 'ciudades', 'fechaCampo', 'conclusiones', 'agencia', 'accionesLogros', 'valorUnitario', 'valorTotal']
    list_display = ['EstadoERP', 'TipoDocumento', 'NombreCliente', 'NoLineas', 'FechaPedido', 'Pedido',
                    'EstadoSiesa', 'PedidoSiesa']

    resource_class = articleResourse
    list_filter = ['EstadoERP']
    #list_per_page = 10


admin.site.register(cliente, articleAdmin)
