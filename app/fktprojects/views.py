import os
import re

from django.conf import settings
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib.admin.utils import quote
from django.utils.translation import gettext_lazy as _
from django import forms
from rest_framework.views import APIView
from generic_chooser.views import ModelChooserViewSet, ModelChooserMixin

from fktprojects.abstract import Abstract


class PDFView(APIView):
    def get(self, request):
        file_path = os.path.join(settings.MEDIA_ROOT, 'files/publication.pdf')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
        raise Http404


class AbstractChooserMixin(ModelChooserMixin):
    def get_unfiltered_object_list(self):
        url = str(self.request.headers['Referer']).rsplit('pages')[-1]
        project_id = re.findall('[0-9]+', url)[-1]
        if project_id:
            objects = self.model.objects.filter(project_id=project_id)
            if self.order_by:
                if isinstance(self.order_by, str):
                    objects = objects.order_by(self.order_by)
                else:
                    objects = objects.order_by(*self.order_by)
            return objects

        return None

    def get_edit_item_url(self, item):
        return reverse('wagtailsnippets:edit', args=('fktprojects.abstract', 'Abstract', quote(item.pk)))


class AbstractChooserViewSet(ModelChooserViewSet):
    icon = 'abstract'
    model = Abstract
    page_title = _("Choose abstract")
    per_page = 5
    order_by = ['research_year']

    chooser_mixin_class = AbstractChooserMixin
