from django.db import models
from django.utils.text import slugify

from wagtail.models import Page, ClusterableModel
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel, HelpPanel
from wagtail.admin.panels import TabbedInterface, ObjectList

from core.enums import Status, Palette, Category
from fktprojects.abstract import Abstract
from fktprojects.publication import Publication
from university.widgets import UniversityChooser


class FKTPage(Page):
    subpage_types = [
        'fktprojects.ProjectPage',
    ]

    max_count = 1

    class Meta:
        verbose_name = 'FKT Project'
        verbose_name_plural = 'FKT Projects'


class ProjectPage(Page):
    parent_page_types = ['fktprojects.FKTPage']

    project_title = models.CharField(
        max_length=100,
        null=True,
        unique=True,
    )

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

    university = models.ForeignKey(
        'university.University',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='page_university',
    )

    user = models.ForeignKey(
        'user.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='page_user',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
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

    @property
    def get_info(self):
        return f'{self.user} created at {self.created_at}'

    content_panels = []
    promote_panels = []
    settings_panels = []

    base_data = [
        FieldPanel('project_title'),
        MultiFieldPanel(
            [
                InlinePanel('finance_project'),
            ], heading='Finance',
        ),
        FieldPanel('university', widget=UniversityChooser, help_text='Choose university from the list above.'),
        FieldPanel('user'),
        FieldPanel('heading'),
        FieldPanel('image'),
        FieldPanel('text'),
    ]

    characteristics = [
        FieldPanel('status'),
        FieldPanel('marker'),
        FieldPanel('project_number'),
        FieldPanel('project_start_date'),
        FieldPanel('project_end_date'),
    ]

    abstract = [
        HelpPanel(template='fktprojects/download_file.html', heading='PDF'),
        MultiFieldPanel(
            [
                InlinePanel('abstract_project', max_num=5),
            ], heading='Abstracts',
        )
    ]

    publication = [
        MultiFieldPanel(
            [
                InlinePanel('publication_project', max_num=10),
            ], heading='Publications',
        )
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(base_data, heading='Base data'),
            ObjectList(characteristics, heading='Characteristics'),
            ObjectList(abstract, heading='Abstracts'),
            ObjectList(publication, heading='Publications'),
        ]
    )

    def clean(self):
        super().clean()
        self.title = self.project_title
        self.slug = slugify(self.project_title)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project Page'
        verbose_name_plural = 'Project Pages'
