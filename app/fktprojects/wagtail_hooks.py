from wagtail.core import hooks

from fktprojects.views import AbstractChooserViewSet
from university.views import UniversityChooserViewSet


@hooks.register('register_admin_viewset')
def register_abstract_chooser_viewset():
    return AbstractChooserViewSet('abstract_chooser', url_prefix='abstract-chooser')


@hooks.register('register_admin_viewset')
def register_university_chooser_viewset():
    return UniversityChooserViewSet('university_chooser', url_prefix='university-chooser')
