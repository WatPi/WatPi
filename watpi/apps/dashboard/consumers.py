from channels import Group
import logging
logging.basicConfig(level=logging.INFO)

def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group("survey").add(message.reply_channel)

def ws_message(message):
    logging.info(message.content['text'])
    # in_msg = json.loads(message.content['text'])
    # in_msg['text']['random'] = random.randint(1,1000)
    # out_msg = json.dumps(in_msg)
    # logging.info(out_msg)
    out_msg = message.content['text']
    Group("survey").send({
        "text": out_msg,
    })
