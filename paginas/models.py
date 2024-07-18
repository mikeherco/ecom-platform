from django.db import models
from wagtail.api import APIField
from wagtail.contrib.settings.models import BaseSiteSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from paginas.blocks import CarruselHistoriaItem
from wagtail import blocks as core_blocks
from wagtail.snippets import blocks as snippets_blocks
from paginas.snippets import ClaseColor, Icono
"""TODO: min_num debe ser mínimo 1 en QA y prod"""


@register_setting
class ConfiguracionSitio(BaseSiteSetting):
    mantenimiento = models.BooleanField(default=True)
    analytics = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ForeignKey('wagtailimages.Image', on_delete=models.PROTECT, null=True, blank=True, related_name='+')
    invitado_login = models.BooleanField(default=False)
    paleta_color = StreamField([
        ('paleta_color', core_blocks.StructBlock([
            ('primario', snippets_blocks.SnippetChooserBlock(ClaseColor, required=True)),
            ('secundario', snippets_blocks.SnippetChooserBlock(ClaseColor, required=True)),
            ('acento', snippets_blocks.SnippetChooserBlock(ClaseColor, blank=True, null=True)),
        ], null=True)),
    ], block_counts={
        'paleta_color': {'min_num': 0, 'max_num': 1}
    }, null=True, use_json_field=True)
    redes_sociales = StreamField([
        ('redes_sociales', core_blocks.StructBlock([
            ('titulo', core_blocks.CharBlock()),
            ('icono', snippets_blocks.SnippetChooserBlock(Icono, required=True)),
            ('url', core_blocks.URLBlock(required=True)),
        ], null=True)),
    ], block_counts={
        'redes_sociales': {'min_num': 0, 'max_num': 4}
    }, null=True, blank=True, use_json_field=True)

    api_fields = [
        APIField('site_id'),
        APIField('mantenimiento'),
        APIField('logo'),
        APIField('invitado_login'),
        APIField('paleta_color'),
        APIField('analytics'),
        APIField('redes_sociales'),
    ]


class Base(Page):
    carrusel = StreamField([
        ("carrusel_item", CarruselHistoriaItem())
    ], block_counts={
        'carrusel_historia_item': {'min_num': 1},
    }, use_json_field=True)

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('carrusel'),
    ]


"""
NavBar
    - Logo -> imageField
    - Color asociado al snippet de Clase color
    - Titulo  (Obligatorio)
    - mostrar_titulo y override cuando hay icono
    - mostrar-buscador
    - tipos paginas para la busqueda del buscador (snippet en streamblock)
    - icono de antDesign!!


SubMenu categos
    - Categorias snippet independiente
    - configurar mostrar en submenu en api

Carrusel
    - Checar Grupo Carrusel y Carrusel Pagina

Pagina Producto
    - promocionar -> meterle un api por type=paginas.Productos & promocionnar=True
    - Hacer primer saque Miguel

Novedades
    - checar api por first-published en type=paginas.Productos

Footer
    - checar Pie de pagina
    - licencia, redes sociales y contacto con direccion

"""