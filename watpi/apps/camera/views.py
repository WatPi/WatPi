# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse
from time import sleep
from server import start_camera
import picamera


def index(request):
    webcam = start_camera()
    context = {'response': webcam, 
               'image': 'images/image2.jpg', 
               'caption': 'Here is your image!', }
    return render(request, 'camera_index.html', context=context)


def snap_photo(request, camera=picamera.PiCamera(resolution=(1024, 768))):
    image = camera.capture('apps/camera/static/images/image2.jpg', resize=(320, 240))
    context = {'image': 'images/image2.jpg',
               'caption': 'Here is your image!', }
    return redirect(reverse('camera:index'))


# def snap_lg_photo(request, camera=picamera.PiCamera(resolution=(1024, 768))):
#     image = camera.capture('image.jpg', resize=(800, 600))
#     context = {'image': image,
#                'caption': 'Here is your smaller image!', }
#     return redirect(reverse('camera:index'))


# def capture_10s_video(request, camera=picamera.PiCamera(resolution=(1024, 768))):
#     video = camera.start_recording('video.h264')
#     sleep(10)
#     video.stop_recording()
#     context = {'video': video,
#                'caption': 'Here is your video clip!', }
#     return redirect(reverse('camera:index'))


# def video_preview(request, camera=picamera.PiCamera(resolution=(1024, 768))):
#     camera.start_preview()
#     camera.vflip = True
#     camera.hflip = True
#     camera.brightness = 60
#     return redirect(reverse('camera:index'))
