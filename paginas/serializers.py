from rest_framework import serializers
from wagtail.api.v2.serializers import PageSerializer

from paginas.blocks import PaletaColorBlock, IconoBlock
from paginas.models import ConfiguracionSitio
from paginas.snippets import Categoria, ClaseColor, Icono


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']


class ClaseColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaseColor
        fields = ['nombre']


class IconoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icono
        fields = ['nombre']


class TextoRicoBlockSerializer(serializers.Serializer):
    texto = serializers.CharField()


class PaletaColorSerializer(serializers.Serializer):
    primario = ClaseColorSerializer()
    secundario = ClaseColorSerializer()
    acento = ClaseColorSerializer()

    def to_representation(self, instance):
        primario = None
        secundario = None
        acento = None
        if instance.value.get('primario'):
            primario = ClaseColorSerializer(instance.value.get('primario')).data.get('nombre')
        if instance.value.get('secundario'):
            secundario = ClaseColorSerializer(instance.value.get('secundario')).data.get('nombre')
        if instance.value.get('acento'):
            acento = ClaseColorSerializer(instance.value.get('acento')).data.get('nombre')

        return {
            'primario': primario,
            'secundario': secundario,
            'acento': acento,
        }


class EnlaceBlockSerializer(serializers.Serializer):
    titulo = serializers.CharField()
    tipo = serializers.ChoiceField(choices=[('pagina', 'Página'), ('url', 'URL'), ('sin_enlace', 'Sin Enlace')])
    pagina = serializers.SerializerMethodField()
    url = serializers.URLField(required=False, allow_null=True)

    @staticmethod
    def get_pagina(obj):
        print('get_pagina', obj)
        pagina = obj['pagina']
        if pagina:
            return {
                'id': pagina.id,
                'title': pagina.title,
                'url': pagina.url
            }
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tipo = instance['tipo']

        if tipo == 'pagina':
            representation['pagina'] = self.get_pagina(instance)
            representation['url'] = None
        elif tipo == 'url':
            representation['url'] = instance['url']
            representation['pagina'] = None
        else:
            representation['pagina'] = None
            representation['url'] = None

        return representation


class ColumnaBlockSerializer(serializers.Serializer):
    titulo = serializers.CharField(max_length=120)
    texto = serializers.SerializerMethodField()
    enlace = serializers.SerializerMethodField()

    @staticmethod
    def get_texto(instance):
        texto_rico_block = instance.value.get('texto')
        if texto_rico_block:
            rich_text = texto_rico_block.get('texto')
            return rich_text.source if rich_text else ''
        return ''

    @staticmethod
    def get_enlace(instance):
        enlaces = instance.value.get('enlace')
        return [EnlaceBlockSerializer(enlace).data for enlace in enlaces]

    def to_representation(self, instance):
        representation = {
            'titulo': instance.value.get('titulo'),
            'texto': self.get_texto(instance),
            'enlace': self.get_enlace(instance),
        }
        return representation


class IconoBlockSerializer(serializers.Serializer):
    icono = IconoSerializer()
    mostrar = serializers.BooleanField()

    def to_representation(self, instance):
        return {
            'icono': instance,
            'mostrar': instance,
        }


class RedesSocialesBlockSerializer(serializers.Serializer):
    icono = IconoBlockSerializer()
    enlace = EnlaceBlockSerializer()

    def to_representation(self, instance):
        return {
            'icono': IconoBlockSerializer(instance.value.get('icono')).data,
            'enlace': EnlaceBlockSerializer(instance.value.get('enlace')).data,
        }


class FooterStreamBlockSerializer(serializers.Serializer):
    columna = serializers.ListSerializer(child=ColumnaBlockSerializer(), allow_empty=True)
    # redes_sociales = serializers.ListSerializer(child=RedesSocialesBlockSerializer(), allow_empty=True)
    licencia = serializers.CharField()

    def to_representation(self, instance):
        representation = {}
        for block in instance:
            if block.block_type == 'columna':
                if 'columna' not in representation:
                    representation['columna'] = []
                representation['columna'].append(ColumnaBlockSerializer(block).data)
            # elif block.block_type == 'redes_sociales':
            #     if 'redes_sociales' not in representation:
            #         representation['redes_sociales'] = []
            #     representation['redes_sociales'].append(RedesSocialesBlockSerializer(block).data)
            elif block.block_type == 'licencia':
                representation['licencia'] = block.value

        return representation


class ConfiguracionSitioSerializer(serializers.ModelSerializer):
    paleta_color = PaletaColorSerializer(many=True)
    footer = FooterStreamBlockSerializer()

    class Meta:
        model = ConfiguracionSitio
        fields = '__all__'
