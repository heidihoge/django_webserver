# -*- coding: utf-8 -*-


from django.contrib import admin

from .models import Producto
from .models import Categoria

admin.site.register(Categoria)

admin.site.register(Producto)
