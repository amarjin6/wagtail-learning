from django.urls import path

from fktprojects.views import PDFView

urlpatterns = [
    path('pdf/download/', PDFView.as_view())
]
