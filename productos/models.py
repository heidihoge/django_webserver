from django.db import models

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    precio = models.IntegerField(default=0)
    categoria = models.CharField(max_length=250)
    producto_foto = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre_producto + ' - ' + str(self.precio)



# class Categoria(models.Model):
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     nombre_categoria = models.CharField (max_length= 250)

