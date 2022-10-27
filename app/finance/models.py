from django.db import models

from wagtail.snippets.models import register_snippet


@register_snippet
class Finance(models.Model):
    grants = models.FloatField(
        null=True,
        default=.0,
    )

    subsides = models.FloatField(
        null=True,
        default=.0,
    )

    securities = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    orders = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    donations = models.FloatField(
        null=True,
        default=.0,
    )

    def __str__(self):
        return self.id
