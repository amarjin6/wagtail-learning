from django.db import models

from wagtail.models import ClusterableModel, Orderable, ParentalKey
from wagtail.admin.edit_handlers import FieldPanel
from modelcluster.fields import ParentalManyToManyField
from wagtailautocomplete.edit_handlers import AutocompletePanel

from core.enums import year_choices, current_year, PublicationType
from fktprojects.abstract import Abstract
from user.models import User


class Publication(ClusterableModel, Orderable):
    abstract = ParentalKey(
        Abstract,
        null=True,
        blank=True,
        related_name='publication_abstract',
    )

    publication_type = models.CharField(
        choices=PublicationType.choices(),
        default=PublicationType.DEFAULT.name,
        null=True,
        max_length=22,
    )

    year = models.IntegerField('year', choices=year_choices(), default=current_year)

    authors = ParentalManyToManyField(
        User,
        blank=True,
        related_name='publication_authors',
    )

    post_title = models.CharField(
        max_length=255,
        null=True,
    )

    post_subtitle = models.CharField(
        max_length=255,
        null=True,
    )

    publication_date = models.DateTimeField(
        null=True,
    )

    page_number = models.IntegerField(
        null=True,
    )

    magazine = models.CharField(
        max_length=100,
        null=True,
    )

    publishing_house = models.CharField(
        max_length=100,
        null=True,
    )

    book_title = models.CharField(
        max_length=100,
        null=True,
    )

    publication_link = models.URLField(
        null=True,
    )

    project = ParentalKey(
        'fktprojects.ProjectPage',
        null=True,
        related_name='publication_project',
    )

    panels = [
        FieldPanel('abstract'),
        FieldPanel('publication_type'),
        FieldPanel('year'),
        AutocompletePanel('authors', target_model=User),
        FieldPanel('post_title'),
        FieldPanel('post_subtitle'),
        FieldPanel('publication_date'),
        FieldPanel('page_number'),
        FieldPanel('magazine'),
        FieldPanel('publishing_house'),
        FieldPanel('book_title'),
        FieldPanel('publication_link'),

    ]

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
