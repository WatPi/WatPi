from channels import Group
import logging, json, base64, os
logging.basicConfig(level=logging.INFO)

def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group("dash").add(message.reply_channel)

def ws_message(message):
    logging.info(len(message.content['text']))
    # out_msg = message.content['text']
    print os.getcwd()
    with open('static/images/dashboard/wheel.jpg', 'rb') as imgfile:
        encoded = base64.b64encode(imgfile.read())
    out = {
        "image": encoded
    }
    out_msg = json.dumps(out)
    Group("dash").send({
        "text": out_msg,
    })
