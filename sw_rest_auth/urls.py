# coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^check_token/$', views.check_token),
    url(r'^check_perm/$', views.check_perm),
]
