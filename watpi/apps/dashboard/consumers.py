from channels import Group
import logging
logging.basicConfig(level=logging.INFO)

def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group("dash").add(message.reply_channel)

def ws_message(message):
    # logging.info(len(message.content['text']))
    out_msg = message.content['text']
    Group("dash").send({
        "text": out_msg,
    })
