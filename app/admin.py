from django.contrib import admin
from .models import  ImagenUsuario


class ImagenUsuarioAdmin(admin.ModelAdmin):
    list_display = ('imagen',)

# Register your models here.

admin.site.register(ImagenUsuario, ImagenUsuarioAdmin)