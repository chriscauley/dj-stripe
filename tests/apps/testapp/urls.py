from django.urls import re_path, include

from django.http import HttpResponse


def empty_view(request):
    return HttpResponse()

urlpatterns = [
    re_path(
        r"^$",
        empty_view,
        name="test_url_name"
    ),
    re_path(r"^djstripe/", include(('djstripe.urls', 'djstripe'), namespace="djstripe")),
    re_path(
        r"^rest_djstripe/",
        include(('djstripe.contrib.rest_framework.urls', 'rest_djstripe'), namespace="rest_djstripe")
    ),
]
