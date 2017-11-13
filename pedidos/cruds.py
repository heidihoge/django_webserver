from models import Pedido, Estados
from electiva3.utils import my_templates
from crudbuilder.abstract import BaseCrudBuilder

class PedidosCrud(BaseCrudBuilder):
    model = Pedido
    search_fields = ['nombre_pedido', 'producto__nombre_producto']
    tables2_fields = ('nombre_pedido','producto')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20
    login_required = True
    permission_required = True
    custom_templates = my_templates

    @classmethod
    def custom_queryset(cls, request, **kwargs):
        """Define your own custom queryset for list view"""
        pedidos = Pedido.objects.all()
        return pedidos

    @classmethod
    def custom_context(cls, request, context, **kwargs):
        """Define your own custom context for list view"""
        context['custom_data'] = "Some custom data"
        return context


class EstadosCrud(BaseCrudBuilder):
    model = Estados
    search_fields = ['nombre_estado']
    tables2_fields = ('nombre_estado',)
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20
    login_required = True
    permission_required = True
    custom_templates = my_templates

    @classmethod
    def custom_queryset(cls, request, **kwargs):
        """Define your own custom queryset for list view"""
        estados = Estados.objects.all()
        return estados

    @classmethod
    def custom_context(cls, request, context, **kwargs):
        """Define your own custom context for list view"""
        context['custom_data'] = "Some custom data"
        return context
