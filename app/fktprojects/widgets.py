from generic_chooser.widgets import AdminChooser
from django.urls import reverse
from django.contrib.admin.utils import quote
from django.utils.translation import gettext_lazy as _

from fktprojects.abstract import Abstract


class AbstractChooser(AdminChooser):
    choose_one_text = _('Choose Abstract')
    choose_another_text = _('Choose another Abstract')
    link_to_chosen_text = _('Edit this Abstract')
    model = Abstract
    choose_modal_url_name = 'abstract_chooser:choose'

    def get_edit_item_url(self, item):
        return reverse('wagtailsnippets:edit', args=('fktprojects.abstract', 'Abstract', quote(item.pk)))
