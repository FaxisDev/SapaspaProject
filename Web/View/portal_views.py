from django.shortcuts import render


def portalView(request):

    return render(request, 'portal.html')