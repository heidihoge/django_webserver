import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from django.db import models

class Pedidos(models.Model):
    nombre_pedido = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre_pedido

class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length=250)


