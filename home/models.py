from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from .blocks import CarruselHistoriaItem


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

