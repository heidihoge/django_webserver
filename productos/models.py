import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from django.db import models

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre_categoria


class Producto(models.Model):
    verbose_name_plural = 'Productos'
    nombre_producto = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    precio = models.IntegerField(default=0)
    producto_foto = models.CharField(max_length=1000)
    categoria = models.ForeignKey(Categoria)

#def __init__(self, nombre_producto, precio):
#      self.nombre_producto = {'nombre_producto': nombre_producto}
#      self.descripcion = {'descripcion': descripcion}
#      self.precio = {'precio': precio}



def __getitem__(self, nombre_producto):
    return self.nombre[nombre_producto]

def __getitem__(self, descripcion):
    return self.nombre[descripcion]


def __getitem__(self, precio):
    return self.nombre[precio]