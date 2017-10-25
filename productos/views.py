from crudbuilder.views import ViewBuilder
from productos.cruds import CategoriaCrud,ProductoCrud

from django.http import HttpResponse
from django.db.utils import OperationalError

try:
    builder = ViewBuilder('productos', 'producto', ProductoCrud)
    builder.generate_crud()
    builder = ViewBuilder('productos', 'categoria', CategoriaCrud)
    builder.generate_crud()
except OperationalError:
    pass # happens when db doesn't exist yet, views.py should be
         # importable without this side effect


def index(request):
    return HttpResponse ("<h1>Electiva3- Esta es la parte de productos <h1>")

