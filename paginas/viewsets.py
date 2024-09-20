from rest_framework import viewsets
from wagtail.api.v2.views import PagesAPIViewSet

from paginas.serializers import CategoriaSerializer
from paginas.snippets import Categoria


class PaginasViewSet(PagesAPIViewSet):
    pass


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        return Categoria.objects.all()
