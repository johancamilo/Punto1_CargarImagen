
from django.shortcuts import render
from .models import ImagenUsuario
from .forms import AgregarImagenforms

# Create your views here.


def home(request):
    images= ImagenUsuario.objects.all()
    data = {
        'form' : AgregarImagenforms(),
        'images' : images
    }
    if request.method == 'POST':
        formulario = AgregarImagenforms(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "SE CARGO LA IMAGEN!"
        else:
            formulario = AgregarImagenforms()
    return render(request, 'app/home.html', data)