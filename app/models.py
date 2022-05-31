from distutils.command.upload import upload
from pyexpat import model
from django.db import models

class ImagenUsuario(models.Model):

    imagen = models.ImageField(upload_to="imagenesUsuarios", null=True)

    def __unicode__(self,):
        return str(self.imagen)

