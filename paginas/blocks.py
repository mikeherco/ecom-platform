from django.db import models
from django.db.models import ForeignKey
from modelcluster.fields import ParentalKey
from wagtail import blocks as core_blocks
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Orderable
from wagtail.snippets import blocks as snippets_blocks
from wagtail.snippets.blocks import SnippetChooserBlock
from paginas.snippets import Icono, ClaseColor, Categoria


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
    accion_clase = snippets_blocks.SnippetChooserBlock(ClaseColor, required=False)
    accion_alineacion = core_blocks.ChoiceBlock(max_length=30, null=True, blank=True, default='izquierda',
                                                choices=(('', 'Alineación'), ('izquierda', 'Izquierda'),
                                                         ('centro', 'Centro'), ('derecha', 'Derecha')))
    icono = snippets_blocks.SnippetChooserBlock(Icono, required=False)
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


class TextoRicoBlock(core_blocks.StructBlock):
    texto = core_blocks.RichTextBlock(null=True, required=False)


class IconoBlock(core_blocks.StructBlock):
    icono = snippets_blocks.SnippetChooserBlock(Icono, required=False)
    mostrar = core_blocks.BooleanBlock(required=True, default=True)


class RedesSocialesBlock(core_blocks.StructBlock):
    icono = IconoBlock(label='Icono')
    enlace = EnlaceBlock()

    api_fields = [
        APIField('icono'),
        APIField('enlace'),
    ]

    class Meta:
        min_num = 1
        max_num = 5


class ColumnaBlock(core_blocks.StructBlock):
    titulo = core_blocks.CharBlock(max_length=120)
    texto = TextoRicoBlock()
    enlace = core_blocks.ListBlock(EnlaceBlock(), min_num=0, max_num=6)


class FooterStreamBlock(core_blocks.StreamBlock):
    columna = ColumnaBlock()
    redes_sociales = RedesSocialesBlock()
    licencia = core_blocks.TextBlock(required=True, null=False, blank=False, default='Licencia Footer')

    class Meta:
        block_counts = {
            'columna': {'min_num': 0, 'max_num': 2},
            'redes_sociales': {'min_num': 0, 'max_num': 5},
            'licencia': {'min_num': 1, 'max_num': 1},
        }


class PaletaColorBlock(core_blocks.StructBlock):
    primario = snippets_blocks.SnippetChooserBlock(ClaseColor, blank=True, null=True)
    secundario = snippets_blocks.SnippetChooserBlock(ClaseColor, blank=True, null=True)
    acento = snippets_blocks.SnippetChooserBlock(ClaseColor, blank=True, null=True)


class CategoriasOrderable(Orderable):
    page = ParentalKey('paginas.Navbar', related_name='navbar_categorias', on_delete=models.CASCADE)
    categoria = ForeignKey(Categoria, on_delete=models.CASCADE)
    mostrar = models.BooleanField(default=True)

    content_panels = [
        SnippetChooserBlock('paginas.Categoria'),
        FieldPanel('mostrar')
    ]
    api_fields = [
        APIField('mostrar'),
        APIField('nombre'),
    ]

    @property
    def nombre(self):
        return self.categoria.nombre
