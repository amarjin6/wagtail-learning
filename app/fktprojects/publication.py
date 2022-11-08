from django.db import models

from wagtail.models import ClusterableModel, Orderable, ParentalKey
from wagtail.admin.edit_handlers import FieldPanel
from modelcluster.fields import ParentalManyToManyField
from wagtailautocomplete.edit_handlers import AutocompletePanel

from core.enums import year_choices, current_year, PublicationType
from fktprojects.abstract import Abstract
from user.models import User
from fktprojects.widgets import AbstractChooser


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

    publication_title = models.CharField(
        max_length=255,
        null=True,
    )

    publication_subtitle = models.CharField(
        max_length=255,
        null=True,
    )

    publication_date = models.DateTimeField(
        null=True,
    )

    newspaper_title = models.CharField(
        max_length=100,
        null=True,
    )

    page_number = models.IntegerField(
        null=True,
    )

    magazine_title = models.CharField(
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
        FieldPanel('publication_title'),
        FieldPanel('abstract', widget=AbstractChooser,
                   help_text='Choices are limited to the current projects\'s abstracts.'),
        FieldPanel('publication_type'),
        FieldPanel('year'),
    ]

    newspaper = [
        FieldPanel('newspaper_title'),
        FieldPanel('page_number'),
    ]

    book = [
        FieldPanel('book_title'),
        FieldPanel('publishing_house'),
        FieldPanel('page_number'),
    ]

    article = [
        AutocompletePanel('authors', target_model=User),
        FieldPanel('magazine_title'),
        FieldPanel('page_number'),
        FieldPanel('publication_date'),
    ]

    internet = [
        FieldPanel('publication_link'),
        FieldPanel('publication_date'),
        FieldPanel('publication_subtitle'),
    ]

    def __str__(self):
        return self.publication_title

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
