# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import json
from time import sleep
from django.urls import reverse
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.decorators import login_required

# rover imports
from .rover import *

# picamera imports
# TODO:
import picamera

# TODO: can we use this??
# @login_required(login_url='/')
def index(request):
    return render(request, 'index.html', context=None)


# ++++++++++++++ rover view section ++++++++++++++
def rover_move(request, direction):
    move_rover(direction)
    print direction
    data = {
        'direction': direction,
    }
    return HttpResponse(json.dumps(data))


def rover_stop(request):
    stop_rover()
    print 'stopped'
    data = {
        'direction': 'stopped',
    }
    return HttpResponse(json.dumps(data))


# +++++++++++++++ picamera view section +++++++++++++++
# def snap_photo(request):
#     pass
#     camera = picamera.PiCamera(resolution=(1024, 768))
#     image = camera.capture(
#         'apps/camera/static/images/image_sm.jpg', resize=(320, 240))
#     context = {'image': 'images/image_sm.jpg', }
#     camera.close()
#     return redirect(reverse('dashboard:index'))


def take_photo(request):
    camera = picamera.PiCamera(resolution=(1024, 768))
    image = camera.capture(
        'apps/camera/static/images/image_lg.jpg', resize=(800, 600))
    data = {
        # 'image': '/static/images/group_selfie.jpg',
        'image': '/static/images/image_lg.jpg',
    }
    camera.close()
    return HttpResponse(json.dumps(data))


# def capture_10s_video(request):
#     pass
#     camera = picamera.PiCamera(resolution=(1024, 768))
#     video = camera.start_recording('apps/camera/static/images/video.h264')
#     sleep(10)
#     camera.stop_recording()
#     camera.close()
#     context = {'video': 'images/video.h264', }
#     return redirect(reverse('dashboard:index'))
