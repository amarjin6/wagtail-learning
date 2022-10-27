from django.db import models

from wagtail.snippets.models import register_snippet


@register_snippet
class University(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,

    )

    acronym = models.CharField(
        max_length=10,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

    def __str__(self):
        return self.acronym
