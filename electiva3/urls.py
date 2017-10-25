
from django.conf.urls import include,url
from django.contrib import admin

from django.views.generic import TemplateView
from crudbuilder.registry import registry

class CrudListView(TemplateView):
    template_name = "cruds.html"
    title = "Registered Cruds"

    def cruds(self):
        return registry.items()

urlpatterns = [

        url(r'^admin/', admin.site.urls),
        url(r'^productos/', include('productos.urls')),
        url(r'^pedidos/', include('pedidos.urls')),
        url(r'^usuarios/', include('usuarios.urls')),
    ]

try:
    crudlist_view = CrudListView.as_view()
    urlpatterns.append(url(r'^$', crudlist_view))
    urlpatterns.append(url(r'^/',  include('crudbuilder.urls')))
except:
    pass