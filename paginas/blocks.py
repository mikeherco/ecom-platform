from wagtail import blocks
from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets import blocks as snippets
from paginas.snippets import Icono, ClaseColor


class Boton(blocks.StructBlock):
    accion_tipo = blocks.ChoiceBlock(required=True, choices=(
        ('', 'Tipo de acción'), ('sin_accion', 'Sin acción'), ('pagina', 'Página'), ('url', 'URL')),
                                          classname='wagtailuiplus__choice-handler '
                                                    'wagtailuiplus__choice-handler--accion_tipo')
    accion_pagina = blocks.PageChooserBlock(required=False,
                                                 classname='wagtailuiplus__choice-handler-target--accion_tipo '
                                                           'wagtailuiplus__choice-handler-hidden-if--url '
                                                           'wagtailuiplus__choice-handler-hidden-if--ancla')
    accion_url = blocks.URLBlock(required=False,
                                      classname='wagtailuiplus__choice-handler-target--accion_tipo '
                                                'wagtailuiplus__choice-handler-hidden-if--pagina '
                                                'wagtailuiplus__choice-handler-hidden-if--ancla')
    accion_texto = blocks.CharBlock(max_length=30, required=False)
    accion_clase = snippets.SnippetChooserBlock(ClaseColor, required=False)
    accion_alineacion = blocks.ChoiceBlock(max_length=30, null=True, blank=True, default='izquierda',
                                                choices=(('', 'Alineación'), ('izquierda', 'Izquierda'),
                                                         ('centro', 'Centro'), ('derecha', 'Derecha')))
    icono = snippets.SnippetChooserBlock(Icono, required=False)
    icono_posicion = blocks.ChoiceBlock(max_length=30, null=True, blank=True, default='izquierda',
                                             choices=(('izquierda', 'Izquierda'), ('derecha', 'Derecha')))


class CarruselHistoriaItem(blocks.StreamBlock):
    imagen = ImageChooserBlock(
        label='Imagen', required=False
    )
    titulo = RichTextBlock(required=False,
                               features=['bold', 'italic', 'superscript', 'subscript', 'strikethrough'])
    descripcion = RichTextBlock(required=False,
                                    features=['bold', 'italic', 'superscript', 'subscript', 'strikethrough', 'link'])

    boton = Boton()

    alineacion_texto = blocks.ChoiceBlock(max_length=30, null=True, blank=True, required=False,
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


