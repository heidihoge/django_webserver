from crudbuilder.views import ViewBuilder
from pedidos.cruds import PedidosCrud

from django.http import HttpResponse

builder = ViewBuilder('pedidos', 'pedidos', PedidosCrud)
builder.generate_crud()

def index(request):
    return HttpResponse ("<h1>Electiva3- Esta es la parte de pedidos <h1>")