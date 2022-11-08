from generic_chooser.views import ModelChooserViewSet
from django.utils.translation import gettext_lazy as _

from university.models import University


class UniversityChooserViewSet(ModelChooserViewSet):
    icon = 'abstract'
    model = University
    page_title = _("Choose university")
    per_page = 5
    order_by = 'name'
    fields = ['name', 'acronym', 'creator', ]
