from django.db import models
from wagtail.models import RevisionMixin, LockableMixin, WorkflowMixin, DraftStateMixin
from django.conf import settings


class RevisionBaseModelMixin(LockableMixin, WorkflowMixin, DraftStateMixin, RevisionMixin, models.Model):
    class Meta:
        abstract = True


AdvancedSnippetMixin = RevisionBaseModelMixin if settings.ENABLE_ADVANCED_SNIPPETS else models.Model
