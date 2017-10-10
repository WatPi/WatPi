# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^take_photo/$', views.snap_photo, name='take_photo'),
    url(r'^take_lg_photo/$', views.snap_lg_photo, name='take_lg_photo'),
    url(r'^take_video/$', views.capture_10s_video, name='take_video'),
    # url(r'^start_preview/$', views.video_preview, name='start_preview'),
]
