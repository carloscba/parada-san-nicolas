from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import horario_list

urlpatterns = [
    url(r'^horario/(?P<pk>[0-9]+)$', horario_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)