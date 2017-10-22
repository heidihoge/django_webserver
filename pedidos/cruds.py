from models import Pedidos

from crudbuilder.abstract import BaseCrudBuilder

class PedidosCrud(BaseCrudBuilder):
    model = Pedidos
    search_fields = ['nombre_pedido']
    tables2_fields = ('nombre_pedido',)
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20
    login_required = True
    permission_required = True

    @classmethod
    def custom_queryset(cls, request, **kwargs):
        """Define your own custom queryset for list view"""
        pedidos = Pedidos.objects.all()
        return pedidos

    @classmethod
    def custom_context(cls, request, context, **kwargs):
        """Define your own custom context for list view"""
        context['custom_data'] = "Some custom data"
        return context


