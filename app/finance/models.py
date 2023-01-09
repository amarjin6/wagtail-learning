from django.db import models

from wagtail.models import ParentalKey


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

    project = ParentalKey(
        'fktprojects.ProjectPage',
        null=True,
        on_delete=models.CASCADE,
        related_name='finance_project')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Finance'
        verbose_name_plural = 'Finances'
