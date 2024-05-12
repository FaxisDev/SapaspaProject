from django.shortcuts import render

# Create your views here.
def portalView(request):

    return render(request, 'portal.html')