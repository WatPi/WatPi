# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse
from time import sleep
# import picamera


# def index(request):
#     context = {'image_sm': 'images/image2.jpg', 
#                'image_lg': 'images/image3.jpg',
#                'caption': 'Here is your image!', }
#     return render(request, 'camera_index.html', context=context)


# def snap_photo(request):
#     camera = picamera.PiCamera(resolution=(1024, 768))
#     image = camera.capture('apps/camera/static/images/image_sm.jpg', resize=(320, 240))
#     context = {'image': 'images/image_sm.jpg',
#                'caption': 'Here is your smaller image!', }
#     camera.close()
#     return redirect(reverse('camera:index'))


# def snap_lg_photo(request):
#     camera = picamera.PiCamera(resolution=(1024, 768))
#     image = camera.capture('apps/camera/static/images/image_lg.jpg', resize=(800, 600))
#     context = {'image': 'images/image_lg.jpg',
#                'caption': 'Here is your bigger image!', }
#     camera.close()
#     return redirect(reverse('camera:index'))


# def capture_10s_video(request):
#     camera = picamera.PiCamera(resolution=(1024, 768))
#     video = camera.start_recording('apps/camera/static/images/video.h264')
#     sleep(10)
#     camera.stop_recording()
#     camera.close()
#     context = {'video': 'images/video.h264',
#                'caption': 'Here is your video clip!', }
#     return redirect(reverse('camera:index'))


# def video_preview(request, camera=picamera.PiCamera(resolution=(1024, 768))):
#     camera.start_preview()
#     camera.vflip = True
#     camera.hflip = True
#     camera.brightness = 60
#     return redirect(reverse('camera:index'))

import io
import os
from google.cloud import vision
from google.cloud.vision import types
    
def annotate_image(request):
    image_labels = []
    client = vision.ImageAnnotatorClient()
    file_name = 'camera/static/images/image_sm.jpg'

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels: ')
    for label in labels:
        print(label.description)
        image_labels.append(label.description)
    return HttpResponse(content=str(image_labels))
