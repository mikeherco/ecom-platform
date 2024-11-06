from django.db import models
from wagtail.api import APIField
from wagtail.contrib.settings.models import BaseSiteSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from paginas.blocks import CarruselHistoriaBlock, FooterStreamBlock, IconoBlock, PaletaColorBlock
from wagtail import blocks as core_blocks
from wagtail.snippets import blocks as snippets_blocks

from paginas.snippets import ClaseColor, Icono
from wagtail.images.blocks import ImageChooserBlock

"""TODO: min_num debe ser mínimo 1 en QA y prod"""


@register_setting
class ConfiguracionSitio(BaseSiteSetting):
    mantenimiento = models.BooleanField(default=True)
    analytics = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ForeignKey('wagtailimages.Image', on_delete=models.PROTECT, null=True, blank=True, related_name='+')
    invitado_login = models.BooleanField(default=False)
    paleta_color = StreamField([
        ('paleta_color', PaletaColorBlock(null=True)),
    ], blank=True, null=True, min_num=0, max_num=1)
    footer = StreamField(FooterStreamBlock(), min_num=0, max_num=4)

    api_fields = [
        APIField('site_id'),
        APIField('mantenimiento'),
        APIField('logo'),
        APIField('invitado_login'),
        APIField('paleta_color'),
        APIField('analytics'),
        # APIField('redes_sociales'),
        APIField('footer'),
    ]

    class Meta:
        verbose_name = 'Configuracion Sitio'
        verbose_name_plural = 'Configuraciones Sitios'


class Base(Page):
    """Base es HOME"""
    carrusel = StreamField([
        ("carrusel_item", CarruselHistoriaBlock())
    ], block_counts={
        'carrusel_item': {'min_num': 1},
    }, use_json_field=True)

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('carrusel'),
    ]
    max_count = 1

    class Meta:
        verbose_name = 'Pagina Base'
        verbose_name_plural = 'Paginas Base'


class Grupo(Page):
    parent_page_types = ['Base']

    subpage_types = ['Navbar']

    class Meta:
        verbose_name = 'Pagina Grupo'
        verbose_name_plural = 'Paginas Grupo'


class NavBar(Page):
    parent_page_types = ['Grupo']

    subpages_type = []

    desc = StreamField([
        ('logo', ImageChooserBlock(required=True)),
        ('color', snippets_blocks.SnippetChooserBlock(ClaseColor, required=True)),
        ('icono', IconoBlock())
    ], block_counts={
        'icono': {'max_num': 1},
    })

    content_panels = Page.content_panels + [
        FieldPanel('desc'),
        MultiFieldPanel(
            [
                InlinePanel('navbar_categorias', label='Categoria'),
            ], heading='Categoria(s)'),
    ]

    promote_panels = Page.promote_panels + []

    api_fields = [
        APIField('desc'),
        APIField('navbar_categorias'),
    ]

    class Meta:
        verbose_name = 'NavBar'
        verbose_name_plural = 'NavBars'


"""
SubMenu categos -> agregar mostrar submenu en config sitio
    - Categorias snippet independiente
    - configurar mostrar en submenu en api

Carrusel
    - Checar Grupo Carrusel y Carrusel Pagina
    - Titulo
    - Descripcion
    - Imagen
    - Boton accion
    - choices Centrado, izquierda, derecha y centro

Pagina Producto
    - promocionar -> meterle un api por type=paginas.Productos & promocionnar=True
    - Hacer primer saque Miguel

Novedades
    - checar api por first-published en type=paginas.Productos

Descuentos como paginas con porcentaje de descuento y streamfield de pagechooser
"""