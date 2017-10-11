# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ++++++++ rover urls ++++++++
    url(r'^rover/move/(?P<direction>[\w]{1,10})$',
        views.rover_move,
        name='rover_move'
        ),
    url(r'^rover/stop$', views.rover_stop, name='rover_stop'),

    # ++++++++ picamera urls ++++++++
    # url(r'^snap_photo/$', views.snap_photo, name='take_photo'),
    url(r'^take_photo/$', views.take_photo, name='take_photo'),
    # url(r'^take_video/$', views.capture_10s_video, name='take_video'),
]
