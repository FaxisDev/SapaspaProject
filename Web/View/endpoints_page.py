# Importa la función `render`, que se utiliza para devolver una respuesta HTML utilizando un template.
from django.shortcuts import render

# Importa `get_resolver`, que se utiliza para obtener el resolvedor de URLs, el cual permite acceder a los patrones de URL configurados en el proyecto.
from django.urls import get_resolver

# Importa `login_required`, un decorador que restringe el acceso a la vista, asegurándose de que el usuario esté autenticado antes de permitir el acceso.
from django.contrib.auth.decorators import login_required

# Aplica el decorador `login_required` a la vista `endPointsView`, lo que significa que solo los usuarios autenticados pueden acceder a esta vista.
@login_required
def endPointsView(request):
    # Obtiene el resolvedor de URLs actual, que contiene todos los patrones de URL definidos en el proyecto.
    resolver = get_resolver()

    # Inicializa una lista vacía que se utilizará para almacenar la información de cada patrón de URL.
    url_patterns = []

    # Itera sobre cada patrón de URL en el resolvedor.
    for url_pattern in resolver.url_patterns:
        # Verifica si el patrón de URL tiene un atributo `name`. Solo se procesan los patrones de URL que tienen un nombre definido.
        if hasattr(url_pattern, 'name'):
            # Crea un diccionario `pattern` que almacena información del patrón de URL.
            pattern = {
                # Almacena el nombre del patrón de URL.
                'name': url_pattern.name,

                # Convierte el patrón de URL a una cadena y lo almacena.
                'url': str(url_pattern.pattern),

                # Almacena los métodos HTTP que el patrón de URL soporta (GET, POST, etc.). Si el patrón de URL tiene una clase de vista (`view_class`), se obtienen los métodos de esa clase. De lo contrario, se intenta derivar los métodos del nombre de la función de la vista.
                'methods': ", ".join(url_pattern.callback.view_class.http_method_names) if hasattr(url_pattern.callback, 'view_class') else ", ".join(url_pattern.callback.__name__.split('_')[0].upper()),

                # Almacena los argumentos por defecto del patrón de URL, si los tiene.
                'default_args': getattr(url_pattern, 'default_args', None),

                # Almacena la cadena de búsqueda (`lookup_str`) asociada con el patrón de URL, que es una representación interna del nombre de la vista o función asociada con esa URL.
                'lookup_str': url_pattern.lookup_str,
            }

            # Añade el diccionario `pattern` a la lista `url_patterns`.
            url_patterns.append(pattern)

    # Renderiza el template `endpoints.html` con el contexto `url_patterns`, que contiene la lista de patrones de URL y su información asociada.
    return render(request, 'endpoints.html', {'url_patterns': url_patterns})
