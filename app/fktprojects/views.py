import os
from django.conf import settings
from django.http import HttpResponse, Http404
from rest_framework.views import APIView


class PDFView(APIView):

    def get(self, request):
        file_path = os.path.join(settings.MEDIA_ROOT, 'documents/publication.pdf')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
        raise Http404
