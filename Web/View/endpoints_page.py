from django.shortcuts import render
from django.urls import get_resolver
from django.contrib.auth.decorators import login_required

@login_required
def endPointsView(request):
    resolver = get_resolver()
    url_patterns = []
    for url_pattern in resolver.url_patterns:
        if hasattr(url_pattern, 'name'):
            pattern = {
                'name': url_pattern.name,
                'url': str(url_pattern.pattern),
                'methods': ", ".join(url_pattern.callback.view_class.http_method_names) if hasattr(url_pattern.callback, 'view_class') else ", ".join(url_pattern.callback.__name__.split('_')[0].upper()),
                'default_args': getattr(url_pattern, 'default_args', None),
                'lookup_str': url_pattern.lookup_str,
            }
            url_patterns.append(pattern)
    return render(request, 'endpoints.html', {'url_patterns': url_patterns})
