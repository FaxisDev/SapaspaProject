from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Web'

    def ready(self):
        from django.contrib import admin
        admin.site.site_title = _("Sapaspa - Panel de Administración")
        admin.site.site_header = _("Panel de administración")
        admin.site.index_title = _("Bienvenido al Pnel de Administración de Agua Potable y Alcantarillado de San Pablo Atlalzalpan")