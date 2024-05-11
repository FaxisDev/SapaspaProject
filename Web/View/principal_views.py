from django.shortcuts import render

# Create your views here.
def principalView(request):
    contexto = {
        'titulo': 'Mi página',
        'contenido': 'Bienvenido a mi página web.'
    }
    return render(request, 'principal.html', contexto)