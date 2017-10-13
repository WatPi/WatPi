# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Google Cloud Vision
from google.cloud import vision
from google.cloud.vision import types

import sys
import io
import os
import json
from time import sleep
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.decorators import login_required
from google.cloud import vision
from google.cloud.vision import types
from .models import *
from ..gallery.consumers import *

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

    data = {
        'img_url': addr[15:],
        'filename': new_name,
    }
    # print(data)
    # print('data url: ')
    # print(data['img_url'])

    # Google Cloud Vision to get annotations
    try: 
        image_labels = []
        client = vision.ImageAnnotatorClient()
        file_name = addr
        # print('file url: ') 
        # print(file_name)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)
        # print('made it to image =')
        response = client.label_detection(image=image)
        labels = response.label_annotations
        # print(labels)

        # Printing labels to console to check 
        print('Labels: ')
        for label in labels:
            print(label.description)
            image_labels.append(label.description)
        top_label = image_labels[0]
        data['label'] = top_label
    except:
        print('This shit does not work.')


    return HttpResponse(json.dumps(data))
