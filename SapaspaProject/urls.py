"""SapaspaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


from Propiedades.views import PropiedadListCreateView, PropiedadDetailView, TipoPropiedadListCreateView, TipoPropiedadDetailView
from Contribuyentes.views import ContribuyenteListCreateView, ContribuyenteDetailView
from Tarifas.views import TarifaListCreateView
from Recibos.views import ReciboListView, ReciboDetailView, PagoListCreateView, PagoDetailView, TipoPagoListView, ObtenerPagosListView, GenerarReciboView
from Servicios.views import TarifaListView
from PreguntasFrecuentes.views import PreguntaFrecuenteListView

from Web.View.principal_views import principalView, PagosPorMesChartView, RecibosPorMesChartView
from Web.View.portal_views import portalView
from Web.View.endpoints_page import endPointsView
from Web.View.Reportes.reporte_pagos_view import reportePagoslView
from Web.View.Reportes.reporte_contribuyentes_view import reporteContribuyentesView
from Web.View.Pdfs.recibo_pdf_view import reciboPDFView

from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(), name='logout'),

    #Seccion Web Administrable
    path('', portalView, name='principal-page'),
    path('principal/', principalView, name='principal-page'),
    path('endpoints/', endPointsView, name='endpoints-page'),
    path('reporte/pagos/', reportePagoslView, name='reporte-pagos-page'),
    path('reporte/contribuyentes/', reporteContribuyentesView, name='reporte-contribuyentes-page'),
    #PDF
    path('pdf/recibo/<recibo_id>/<contribuyente_id>/', reciboPDFView, name='Recibo de agua PDF'),
    #Graficos
    path('chart/pagos-por-mes/', PagosPorMesChartView.as_view(), name='pagos_por_mes_chart'),
    path('chart/recibos-por-mes/', RecibosPorMesChartView.as_view(), name='recibos_por_mes_chart'),
    #Seccion de API
    path('api/propiedades/', PropiedadListCreateView.as_view(), name='propiedad-list-create'),
    path('api/propiedades/<int:pk>/', PropiedadDetailView.as_view(), name='propiedad-detail'),
    path('api/tipo-propiedades', TipoPropiedadListCreateView.as_view(), name='tipo-propiedad-list-create'),
    path('api/tipo-propiedades/<int:pk>/', TipoPropiedadDetailView.as_view(), name='tipo-propiedad-detail'),
    path('api/contribuyentes', ContribuyenteListCreateView.as_view(), name='contribuyente-list-create'),
    path('api/contribuyentes/<int:pk>/', ContribuyenteDetailView.as_view(), name='contribuyente-detail'),
    path('api/tarifas', TarifaListCreateView.as_view(), name='tarifa-list-create'),
    path('api/tipo-pagos', TipoPagoListView.as_view(), name='Ver lista de tipo de Pagos'),
    path('api/recibos', ReciboListView.as_view(), name='Crear y ver lista de Recibos'),
    path('api/recibos/<int:pk>/', ReciboDetailView.as_view(), name='Ver detalle de Recibos'),
    path('api/pago', PagoListCreateView.as_view(), name='Crear y ver lista de Pagos'),
    path('api/pago/<int:pk>/', PagoDetailView.as_view(), name='Ver detalle de Pagos'),
    path('api/obtener-pago', ObtenerPagosListView.as_view(), name='Obtener lista pagos pendientes'),
    path('api/generar-recibo',GenerarReciboView.as_view(), name='Generar recibo con pagos'),
    path('api/servicios/', TarifaListView.as_view(), name='propiedad-list'),
    path('api/preguntas-frecuentes/', PreguntaFrecuenteListView.as_view(), name='Lista de Preguntas Frecuentes'),   
]
