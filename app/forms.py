from django import forms
from .models import ImagenUsuario

class AgregarImagenforms(forms.ModelForm):
    class Meta:
        model = ImagenUsuario
        fields = ['imagen']

