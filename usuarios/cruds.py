from models import Usuarios
from electiva3.utils import my_templates
from crudbuilder.abstract import BaseCrudBuilder

class UsuarioCrud(BaseCrudBuilder):
    model = Usuarios
    search_fields = ['nombre_usuario']
    tables2_fields = ('nombre_usuario', )
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20
    login_required = True
    permission_required = True
    custom_templates = my_templates

    @classmethod
    def custom_queryset(cls, request, **kwargs):
        """Define your own custom queryset for list view"""
        usuarios = Usuarios.objects.all()
        return usuarios

    @classmethod
    def custom_context(cls, request, context, **kwargs):
        """Define your own custom context for list view"""
        context['custom_data'] = "Some custom data"
        return context

