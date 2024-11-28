from django.db import models
from wagtail.blocks.struct_block import StructBlock
from wagtail.fields import StreamField
from wagtail.models import RevisionMixin, LockableMixin, WorkflowMixin, DraftStateMixin
from django.conf import settings
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.models import Page

from paginas.snippets import Color


class RevisionBaseModelMixin(LockableMixin, WorkflowMixin, DraftStateMixin, RevisionMixin, models.Model):
    class Meta:
        abstract = True


class LogoMixin(models.Model):
    logo = models.ForeignKey('wagtailimages.Image', on_delete=models.PROTECT,
                             null=True, blank=True, related_name='+')

    api_fields = [
        'logo'
    ]

    class Meta:
        abstract = True


class PaletaColorMixin(models.Model):
    paleta_color = StructBlock([
        ('primario', SnippetChooserBlock(Color, required=True)),
        ('secundario', SnippetChooserBlock(Color, required=True)),
        ('acento', SnippetChooserBlock(Color, required=True)),
    ], null=True, blank=True, use_json_field=True)

    api_fields = [
        'paleta_color',
    ]

    content_panels = [
        'paleta_color'
    ]

    class Meta:
        abstract = True


AdvancedSnippetMixin = RevisionBaseModelMixin if settings.ENABLE_ADVANCED_SNIPPETS else models.Model
