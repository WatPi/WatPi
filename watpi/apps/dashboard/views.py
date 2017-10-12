# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import os
import json
from time import sleep
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.decorators import login_required
from .models import *

# rover imports
from .rover import *

# picamera imports
# TODO:
import picamera


@login_required(login_url='/login')
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
# TODO: do we need this?????
# def snap_photo(request):
#     pass
#     camera = picamera.PiCamera(resolution=(1024, 768))
#     image = camera.capture(
#         'apps/camera/static/images/image_sm.jpg', resize=(320, 240))
#     context = {'image': 'images/image_sm.jpg', }
#     camera.close()
#     return redirect(reverse('dashboard:index'))


def take_photo(request):
    number_of_photos_stored = Photo.objects.all().count()
    new_name = 'img_' + str(timezone.now())[:26] + '.jpg'
    new_name = new_name.replace(' ', '_')
    new_time_created = timezone.now()
    addr = 'apps/dashboard/static/dashboard/images/' + new_name

    if number_of_photos_stored == 10:
        # rewrite the oldest photo, cap the number of photos at 10
        photo_to_rw = Photo.objects.order_by('time_created').first()
        photo_to_delete = photo_to_rw.name
        path_to_delete = 'apps/dashboard/static/dashboard/images/' + photo_to_delete
        os.remove(path_to_delete) 

        photo_to_rw.update()

    else:
        Photo.objects.create(name=new_name, time_created=new_time_created)

    camera = picamera.PiCamera(resolution=(1024, 768))
    image = camera.capture(addr, resize=(800, 600))
    camera.close()

    # Google Drive save path
    img_path_to_save = 'static' + addr[22:]
    data = {
        'img_url': addr[15:],
        'img_path_to_save': img_path_to_save,
        'filename': new_name,
    }

    print(data)

    return HttpResponse(json.dumps(data))


# def capture_10s_video(request):
# TODO do we need???????
#     pass
#     camera = picamera.PiCamera(resolution=(1024, 768))
#     video = camera.start_recording('apps/camera/static/images/video.h264')
#     sleep(10)
#     camera.stop_recording()
#     camera.close()
#     context = {'video': 'images/video.h264', }
#     return redirect(reverse('dashboard:index'))
