from django.db import models

from wagtail.models import Page, ClusterableModel
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.snippets.models import register_snippet

from core.enums import Status, Palette, Category, year_choices, current_year, PublicationType


class FKTPage(Page):
    subpage_types = [
        'fktprojects.ProjectPage',
    ]


class ProjectPage(Page):
    status = models.CharField(
        max_length=10,
        choices=Status.choices(),
        default=Status.DEFAULT.name,
        null=True,
    )

    marker = models.CharField(
        choices=Palette.choices(),
        default=Palette.RED.name,
        null=True,
        max_length=5,
    )

    financing_source = models.ForeignKey(
        'finance.Finance',
        null=True,
        on_delete=models.SET_NULL,
        related_name='page_financing_source',
    )

    university = models.ForeignKey(
        'university.University',
        null=True,
        on_delete=models.SET_NULL,
        related_name='page_university',
    )

    user = models.ForeignKey(
        'user.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='page_user',
    )

    heading = models.CharField(
        max_length=100,
        null=True,
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    project_number = models.IntegerField(
        null=True,
    )

    project_start_date = models.DateField(
        null=True,
    )

    project_end_date = models.DateField(
        null=True,
    )

    text = models.TextField(
        null=True,
    )

    category = models.CharField(
        choices=Category.choices(),
        default=Category.DEFAULT.name,
        null=True,
        max_length=22,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('status'),
                FieldPanel('marker'),
                FieldPanel('financing_source'),
                FieldPanel('university'),
                FieldPanel('user'),
                FieldPanel('heading'),
                FieldPanel('image'),
                FieldPanel('project_number'),
                FieldPanel('project_start_date'),
                FieldPanel('project_end_date'),
                FieldPanel('text'),
                FieldPanel('category'),
            ],
            heading='Project'
        )
    ]

    def __str__(self):
        return self.title


@register_snippet
class Abstract(ClusterableModel):
    text = models.TextField(
        null=True,
    )

    category = models.CharField(
        choices=Category.choices(),
        default=Category.DEFAULT.name,
        null=True,
        max_length=22,
    )

    research_year = models.IntegerField(('year'), choices=year_choices(), default=current_year)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('text'),
            FieldPanel('category'),
            FieldPanel('research_year'),
        ], heading='Abstract'),
    ]

    def __str__(self):
        return self.text


@register_snippet
class Publications(ClusterableModel):
    abstract = models.ForeignKey(
        'fktprojects.Abstract',
        null=True,
        on_delete=models.SET_NULL,
        related_name='publications_abstract',
    )

    publication_type = models.CharField(
        choices=PublicationType.choices(),
        default=PublicationType.DEFAULT.name,
        null=True,
        max_length=22,
    )

    year = models.IntegerField(('year'), choices=year_choices(), default=current_year)

    author = models.CharField(
        max_length=64,
        null=True,
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

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('abstract'),
            FieldPanel('publication_type'),
            FieldPanel('year'),

            FieldPanel('author'),
            FieldPanel('post_title'),
            FieldPanel('post_subtitle'),
            FieldPanel('publication_date'),

            FieldPanel('page_number'),
            FieldPanel('magazine'),
            FieldPanel('publishing_house'),
            FieldPanel('book_title'),
            FieldPanel('publication_link'),

        ], heading='Publications'),
    ]

    def __str__(self):
        return self.post_title
