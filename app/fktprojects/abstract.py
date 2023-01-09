from django.db import models

from wagtail.models import ClusterableModel, Orderable, ParentalKey
from wagtail.admin.edit_handlers import FieldPanel

from core.enums import year_choices, current_year, Category


class Abstract(ClusterableModel, Orderable):
    text = models.TextField(
        null=True,
    )

    category = models.CharField(
        choices=Category.choices(),
        default=Category.DEFAULT.name,
        null=True,
        max_length=22,
    )

    research_year = models.IntegerField('year', choices=year_choices(), default=current_year)

    project = ParentalKey(
        'fktprojects.ProjectPage',
        null=True,
        related_name='abstract_project',
    )

    panels = [
        FieldPanel('text'),
        FieldPanel('category'),
        FieldPanel('research_year'),
    ]

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Abstract'
        verbose_name_plural = 'Abstracts'
