import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models
from usuarios.models import Usuarios
from productos.models import Producto


class Estados(models.Model):
    nombre_estado = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_estado


class Pedido(models.Model):
    nombre_pedido = models.CharField(max_length=250)
    usuario = models.ForeignKey(Usuarios,default="1")
    num_pedido = models.CharField(max_length=15,default="1")
    producto = models.ForeignKey(Producto, default="")
    concepto = models.CharField(max_length=200,blank=True)
    estado = models.ForeignKey(Estados)
    telefono_ubicacion = models.CharField(max_length=12, blank=True)
    forma_de_recepcion = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return  "Pedido nro: " + str(self.num_pedido)

class EstadosPedidos(models.Model):
   num_pedido = models.ForeignKey(Pedido, default="1")
   estado = models.ForeignKey(Estados)

