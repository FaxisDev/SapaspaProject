from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required # type: ignore
def principalView(request):
    contexto = {
        'titulo': 'Mi página',
        'contenido': 'Bienvenido a mi página web.'
    }
    return render(request, 'principal.html', contexto)