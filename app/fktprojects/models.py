from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel

from core.enums import Status, Palette, Category


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
