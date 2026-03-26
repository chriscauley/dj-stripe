from django.urls import re_path

from django.http import HttpResponse


def testview(request):
    return HttpResponse()

urlpatterns = [
    re_path(
        r"^$",
        testview,
        name="test_url_namespaced",
    ),
]
