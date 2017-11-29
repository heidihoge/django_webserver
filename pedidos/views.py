from crudbuilder.views import ViewBuilder
from pedidos.cruds import PedidosCrud

from django.db.utils import OperationalError

from django.http import HttpResponse


try:
    builder = ViewBuilder('pedidos', 'pedido', PedidosCrud)
    builder.generate_crud()
except OperationalError:
    pass # happens when db doesn't exist yet, views.py should be
         # importable without this side effect


def index(request):
    return HttpResponse ("<h1>Electiva3- Esta es la parte de productos <h1>")