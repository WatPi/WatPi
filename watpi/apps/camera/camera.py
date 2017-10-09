# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import sleep
import picamera


class Camera(object):
    self.camera = picamera.PiCamera()
    self.camera.resolution = (1024, 768)

    def snap_sm_photo(self):
        self.camera.capture('image.jpg', resize=(320, 240))

    def snap_lg_photo(self):
        self.camera.capture('image.jpg', resize=(800, 600))

    def capture_10s_video(self):
        camera.start_recording('video.h264')
        sleep(10)
        camera.stop_recording()

    def video_preview(self):
        camera.start_preview()
        camera.vflip = True
        camera.hflip = True
        camera.brightness = 60

    def __init__(self):
        camera.start_preview()
        sleep(1)

Camera.snap_sm_photo()
