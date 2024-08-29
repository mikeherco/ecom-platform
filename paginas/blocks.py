from django.db import models
from django.db.models import ForeignKey
from modelcluster.fields import ParentalKey
from wagtail import blocks as core_blocks
from wagtail.api import APIField
from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Orderable
from wagtail.snippets import blocks as snippets
from wagtail.snippets.blocks import SnippetChooserBlock
from paginas.snippets import Icono, ClaseColor


class BotonBlock(core_blocks.StructBlock):
    accion_tipo = core_blocks.ChoiceBlock(required=True, choices=(
        ('', 'Tipo de acción'), ('sin_accion', 'Sin acción'), ('pagina', 'Página'), ('url', 'URL')),
                                          classname='wagtailuiplus__choice-handler '
                                                    'wagtailuiplus__choice-handler--accion_tipo')
    accion_pagina = core_blocks.PageChooserBlock(required=False,
                                                 classname='wagtailuiplus__choice-handler-target--accion_tipo '
                                                           'wagtailuiplus__choice-handler-hidden-if--url '
                                                           'wagtailuiplus__choice-handler-hidden-if--ancla')
    accion_url = core_blocks.URLBlock(required=False,
                                      classname='wagtailuiplus__choice-handler-target--accion_tipo '
                                                'wagtailuiplus__choice-handler-hidden-if--pagina '
                                                'wagtailuiplus__choice-handler-hidden-if--ancla')
    accion_texto = core_blocks.CharBlock(max_length=30, required=False)
    accion_clase = snippets.SnippetChooserBlock(ClaseColor, required=False)
    accion_alineacion = core_blocks.ChoiceBlock(max_length=30, null=True, blank=True, default='izquierda',
                                                choices=(('', 'Alineación'), ('izquierda', 'Izquierda'),
                                                         ('centro', 'Centro'), ('derecha', 'Derecha')))
    icono = snippets.SnippetChooserBlock(Icono, required=False)
    icono_posicion = core_blocks.ChoiceBlock(max_length=30, null=True, blank=True, default='izquierda',
                                             choices=(('izquierda', 'Izquierda'), ('derecha', 'Derecha')))


class CarruselHistoriaBlock(core_blocks.StreamBlock):
    imagen = ImageChooserBlock(label='Imagen', required=False)
    titulo = RichTextBlock(required=False, features=['bold', 'italic', 'superscript', 'subscript', 'strikethrough'])
    descripcion = RichTextBlock(required=False, features=['bold', 'italic', 'superscript', 'subscript',
                                                          'strikethrough', 'link'])
    boton = BotonBlock()
    alineacion_texto = core_blocks.ChoiceBlock(max_length=30, null=True, blank=True, required=False,
                                               choices=(('izquierda', 'Izquierda'),
                                                        ('derecha', 'Derecha')), default='izquierda', )

    class Meta:
        icon = 'image'
        block_counts = {
            'imagen': {'min_num': 0, 'max_num': 1},
            'titulo': {'min_num': 0, 'max_num': 1},
            'descripcion': {'min_num': 0, 'max_num': 1},
        }
        label = "Elemento de Carrusel Historia"


class EnlaceBlock(core_blocks.StructBlock):
    titulo = core_blocks.CharBlock()
    tipo = core_blocks.ChoiceBlock(required=True, choices=[('pagina', 'Página'), ('url', 'URL'),
                                                           ('sin_enlace', 'Sin Enlace')], default='pagina')
    pagina = core_blocks.PageChooserBlock(null=True, blank=True, required=False)
    url = core_blocks.URLBlock(null=True, blank=True, required=False)

    api_field = [
        APIField('titulo'),
        APIField('tipo'),
        APIField('pagina'),
        APIField('url'),
    ]

    class Meta:
        icon = 'link'
        label = 'Enlace'
        classname = 'enlace'


class TextoColumnaBlock(core_blocks.StructBlock):
    titulo = core_blocks.CharBlock(required=False)
    texto = core_blocks.RichTextBlock(required=False)

    # class Meta:
    #     icon = 'text'
    #


class LinkBlock(core_blocks.StructBlock):
    enlace = core_blocks.ListBlock(EnlaceBlock(), min_num=1, max_num=5)


class TextoRicoBlock(core_blocks.StructBlock):
    texto = core_blocks.RichTextBlock(null=True, required=False)


class FooterStreamBlock(core_blocks.StreamBlock):
    texto_columna = TextoColumnaBlock()
    link_columna = LinkBlock()
    licencia = TextoRicoBlock()

    class Meta:
        block_counts = {
            'texto_columna': {'min_num': 1, 'max_num': 1},
            'link_columna': {'min_num': 1, 'max_num': 5},
            'licencia': {'min_num': 1, 'max_num': 1},
        }



# class CategoriasOrderable(Orderable):
#     page = ParentalKey('paginas.Navbar', related_name='navbar_categorias')
#     categoria = ForeignKey(Categoria, on_delete=models.CASCADE)
#
#     content_panels = [
#         SnippetChooserBlock('paginas.Categoria'),
#     ]
#     api_fields = [
#         APIField('categoria'),
#     ]
