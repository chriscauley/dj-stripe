# -*- coding: utf-8 -*-
from django.urls import include, re_path
from django.contrib import admin
from django.http.response import HttpResponse


def empty_view(request):
    return HttpResponse

urlpatterns = [
    re_path(r'^home/', empty_view, name="home"),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^djstripe/', include(('djstripe.urls', 'djstripe'), namespace="djstripe")),
    re_path(r'^testapp/', include('tests.apps.testapp.urls')),
    re_path(r'^__debug__/', include('tests.apps.testapp.urls')),
    re_path(
        r'^testapp_namespaced/',
        include(('tests.apps.testapp_namespaced.urls', 'testapp_namespaced'),
        namespace="testapp_namespaced")),

    # Represents protected content
    re_path(r'^testapp_content/', include('tests.apps.testapp_content.urls')),
    # For testing fnmatches
    re_path(
        r"test_fnmatch/extra_text/$",
        empty_view,
        name="test_fnmatch"
    ),
]
