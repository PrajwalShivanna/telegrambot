from telegram.ext import Updater,CommandHandler
from Adafruit_IO import Client, Data
import os
x = os.getenv('x') # ADAFRUIT_IO_USERNAME
y = os.getenv('y') # ADAFRUIT_IO_KEY
z = os.getenv('z') # TELEGRAM_BOT_TOKEN


def on(bot,update):
    chat_id=update.message.chat_id
    bot.send_photo(chat_id,photo='https://previews.123rf.com/images/murika/murika1511/murika151100069/48123160-bright-glowing-incandescent-light-bulb-on-a-white-background.jpg')
    bot.send_message(chat_id,text='bulb turned on')
    aio = Client(x,y)
    value=Data(value=1)
    value_send=aio.create_data('lightningbot',value)

def off(bot,update):
    chat_id=update.message.chat_id
    bot.send_photo(chat_id,photo='https://previews.123rf.com/images/ericmilos/ericmilos0912/ericmilos091200136/6109526-3d-render-of-light-bulb-on-white.jpg')
    bot.send_message(chat_id,text='bulb turned off')
    aio = Client(x,y)
    value=Data(value=0)
    value_send=aio.create_data('lightningbot',value)

up=Updater(z)
disp=up.dispatcher
disp.add_handler(CommandHandler('on',on))
disp.add_handler(CommandHandler('off',off))
up.start_polling()
up.idle()
