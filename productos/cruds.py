from models import Producto, Categoria

from electiva3.utils import my_templates
from crudbuilder.abstract import BaseCrudBuilder

class ProductoCrud(BaseCrudBuilder):
    model = Producto
    search_fields = ['nombre_producto','descripcion']
    tables2_fields = ('nombre_producto', 'categoria', 'descripcion', 'precio', 'producto_foto')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20
    login_required = True
    permission_required = True
    custom_templates = my_templates

    @classmethod
    def custom_queryset(cls, request, **kwargs):
        """Define your own custom queryset for list view"""
        productos = Producto.objects.all()
        return productos

    @classmethod
    def custom_context(cls, request, context, **kwargs):
        """Define your own custom context for list view"""
        context['custom_data'] = "Some custom data"
        return context


class CategoriaCrud(BaseCrudBuilder):
    model = Categoria
    search_fields = ['nombre_categoria']
    tables2_fields = ('nombre_categoria',)
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20
    login_required = True
    permission_required = True
    custom_templates = my_templates

    @classmethod
    def custom_queryset(cls, request, **kwargs):
        """Define your own custom queryset for list view"""
        categoria = Categoria.objects.all()
        return categoria

    @classmethod
    def custom_context(cls, request, context, **kwargs):
        """Define your own custom context for list view"""
        context['custom_data'] = "Some custom data"
        return context


