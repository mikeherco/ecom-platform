from django.db import models
from wagtail.api import APIField
from wagtail.snippets.models import register_snippet


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
    nombre = models.CharField(max_length=120, primary_key=True)

    api_fields = [
        APIField("nombre"),
    ]

    def __str__(self):
        return self.nombr