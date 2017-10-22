import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from django.db import models


class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length=250, default="")
    correo_electronico = models.CharField(max_length=300, default= "")
    password = models.CharField(max_length=30,default="12345")
    rol = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.nombre_usuario