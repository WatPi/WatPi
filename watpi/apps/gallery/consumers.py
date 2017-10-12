import logging, json, base64, os
from channels import Group
from ..dashboard.models import *

logging.basicConfig(level=logging.INFO)

def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group("dash").add(message.reply_channel)

def ws_message(message):
    logging.info(len(message.content['text']))
    print os.getcwd()

    lasted_photo_name = Photo.objects.order_by('-time_created').first().name
    latest_photo_path = 'apps/dashboard/static/dashboard/images/' + lasted_photo_name

    with open(latest_photo_path, 'rb') as imgfile:
        encoded = base64.b64encode(imgfile.read())
    out = {
        "image": encoded
    }
    out_msg = json.dumps(out)
    Group("dash").send({
        "text": out_msg,
    })

    # TODO: out_msg????
