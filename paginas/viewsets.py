from rest_framework import viewsets
from wagtail.api.v2.views import PagesAPIViewSet

from paginas.models import ConfiguracionSitio
from paginas.serializers import CategoriaSerializer, ConfiguracionSitioSerializer, IconoSerializer, ClaseColorSerializer
from paginas.snippets import Categoria, Icono, ClaseColor


class PaginasViewSet(PagesAPIViewSet):
    pass


class ConfiguracionSitioViewSet(viewsets.ModelViewSet):
    serializer_class = ConfiguracionSitioSerializer

    def get_queryset(self):
        return ConfiguracionSitio.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        return Categoria.objects.all()


class ClaseColorViewSet(viewsets.ModelViewSet):
    serializer_class = ClaseColorSerializer

    def get_queryset(self):
        return ClaseColor.objects.all()

