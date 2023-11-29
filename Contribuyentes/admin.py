from django.contrib import admin

# Register your models here.
from .models import Contribuyente

class ContribuyenteAdmin(admin.ModelAdmin):
    search_fields = ['nombre'] #Busqueda de filtro

admin.site.register(Contribuyente, ContribuyenteAdmin)