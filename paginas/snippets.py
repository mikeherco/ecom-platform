from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.snippets.models import register_snippet
from paginas.mixins import RevisionBaseModelMixin
from django.forms import widgets

from colorful.fields import RGBColorField

class ColorPickerWidget(widgets.TextInput):
    input_type = 'color'


@register_snippet
class Icono(models.Model):
    nombre = models.CharField(max_length=120, primary_key=True)

    api_fields = [
        APIField("nombre"),
    ]

    def __str__(self):
        return self.nombre


@register_snippet
class ClaseColor(models.Model):
    color = RGBColorField(default="#FF0000", primary_key=True, help_text="Por favor seleccione un color")


    api_fields = [
        FieldPanel('color'),
    ]

    def __str__(self):
        return self.color



@register_snippet
class Categoria(RevisionBaseModelMixin):
    nombre = models.CharField(max_length=120, null=True, blank=True)

    panels = [
        FieldPanel('nombre'),
    ]

    def __str__(self):
        return self.nombre
