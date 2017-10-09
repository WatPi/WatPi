# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import picamera
from time import sleep

"""
camera = picamera.PiCamera()
camera.capture('image.jpg')

camera.start_preview()
camera.vflip = True
camera.hflip = True
camera.brightness = 60

camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()


from time import sleep
from picamera import PiCamera

def take_image(self):
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('foo.jpg', resize=(320, 240))
"""

"""
This script uses the Vision API's label detection capabilities to find a label
based on an image's content.
"""

import argparse
import base64
import picamera
import json

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


class FindImageLabels:

    def takephoto():
        camera = picamera.PiCamera()
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        sleep(2)
        camera.capture('image.jpg', resize=(320, 240))

    def main():
        takephoto() # First take a picture
        """Run a label request on a single image"""

        credentials = GoogleCredentials.get_application_default()
        service = discovery.build('vision', 'v1', credentials=credentials)

        with open('image.jpg', 'rb') as image:
            image_content = base64.b64encode(image.read())
            service_request = service.images().annotate(body={
                'requests': [{
                    'image': {
                        'content': image_content.decode('UTF-8')
                    },
                    'features': [{
                        'type': 'LABEL_DETECTION',
                        'maxResults': 10
                    }]
                }]
            })
            response = service_request.execute()
            print json.dumps(response, indent=4, sort_keys=True)	#Print it out and make it somewhat pretty.

if __name__ == '__main__':
    FindImageLabels.main()
