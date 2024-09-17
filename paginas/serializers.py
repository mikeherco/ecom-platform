from rest_framework import serializers
from wagtail.api.v2.serializers import StreamField
from paginas.models import NavBar
from paginas.blocks import CategoriasOrderable
from paginas.snippets import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']


class CategoriaOrderableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasOrderable
        fields = ['categoria', 'mostrar']


class NavbarSerializer(serializers.ModelSerializer):
    desc = StreamField()
    navbar_categorias = CategoriaOrderableSerializer(many=True)

    class Meta:
        model = NavBar
        fields = ['title', 'desc', 'navbar_categorias']

