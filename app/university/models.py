from django.db import models

from wagtail.admin.edit_handlers import FieldPanel

from user.models import User


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

    creator = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='university_creator',
    )

    @property
    def get_info(self):
        return f'{self.creator} created at {self.created_at}'

    panels = [
        FieldPanel('name'),
        FieldPanel('acronym'),
        FieldPanel('created_at'),
        FieldPanel('creator'),
    ]

    def __str__(self):
        return self.acronym

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'
