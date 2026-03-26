# -*- coding: utf-8 -*-
"""
Wire this into the root URLConf this way::

    re_path(r'^stripe/', include('djstripe.urls', namespace="djstripe")),
    # url can be changed
    # Call to 'djstripe.urls' and 'namespace' must stay as is

Call it from reverse()::

    reverse("djstripe:subscribe")

Call from url tag::

    {% url 'djstripe:subscribe' %}

"""

from django.urls import re_path

from . import settings as app_settings
from . import views


urlpatterns = [

    # HTML views
    re_path(
        r"^$",
        views.AccountView.as_view(),
        name="account"
    ),
    re_path(
        r"^subscribe/$",
        views.SubscribeView.as_view(),
        name="subscribe"
    ),
    re_path(
        r"^confirm/(?P<plan>.+)$",
        views.ConfirmFormView.as_view(),
        name="confirm"
    ),
    re_path(
        r"^change/plan/$",
        views.ChangePlanView.as_view(),
        name="change_plan"
    ),
    re_path(
        r"^change/cards/$",
        views.ChangeCardView.as_view(),
        name="change_card"
    ),
    re_path(
        r"^cancel/subscription/$",
        views.CancelSubscriptionView.as_view(),
        name="cancel_subscription"
    ),
    re_path(
        r"^history/$",
        views.HistoryView.as_view(),
        name="history"
    ),


    # Web services
    re_path(
        r"^a/sync/history/$",
        views.SyncHistoryView.as_view(),
        name="sync_history"
    ),

    # Webhook
    re_path(
        app_settings.DJSTRIPE_WEBHOOK_URL,
        views.WebHook.as_view(),
        name="webhook"
    ),
]
