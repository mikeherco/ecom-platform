from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.api import APIField
from wagtail.snippets.models import register_snippet
from paginas.mixins import RevisionBaseModelMixin
from django.forms import widgets
from django.core.exceptions import ValidationError
import re

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
    nombre = models.CharField(
        max_length=10,
        choices=[
            ('name', 'Nombre'),
            ('hex', 'Hexadecimal'),
        ],
        help_text="Selecciona el tipo de color: Nombre o Hexadecimal"
    )
    color = models.CharField(
        primary_key=True,
        max_length=10,
        help_text="Proporciona un nombre de color (por ejemplo, 'red') o un código hexadecimal (por ejemplo, '#FF5733')."
    )

    api_fields = [
        FieldPanel('nombre'),
        FieldPanel('color'),
    ]

    def __str__(self):
        return self.color

    def clean(self):
        if self.nombre == "name":
            if not re.match(r'^[a-zA-Z]+$', self.color):
                raise ValidationError("El color debe ser un nombre válido (por ejemplo, 'red', 'blue').")
        elif self.nombre == "hex":
            if not re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', self.color):
                raise ValidationError(
                    "El código hexadecimal debe comenzar con '#' y contener 3 o 6 caracteres hexadecimales.")


@register_snippet
class Categoria(RevisionBaseModelMixin):
    nombre = models.CharField(max_length=120, null=True, blank=True)

    panels = [
        FieldPanel('nombre'),
    ]

    def __str__(self):
        return self.nombre
