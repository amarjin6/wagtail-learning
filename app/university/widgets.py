from generic_chooser.widgets import AdminChooser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.utils import quote

from university.models import University


class UniversityChooser(AdminChooser):
    choose_one_text = _('Choose University')
    choose_another_text = _('Choose another University')
    link_to_chosen_text = _('Edit this University')
    model = University
    choose_modal_url_name = 'university_chooser:choose'

    def get_edit_item_url(self, item):
        return reverse('wagtailsnippets:edit', args=('university.models', 'University', quote(item.pk)))
