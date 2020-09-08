from telegram.ext import Updater,CommandHandler
from Adafruit_IO import Client, Data
import os
x = os.getenv('x') # ADAFRUIT_IO_USERNAME
y = os.getenv('y') # ADAFRUIT_IO_KEY
z = os.getenv('z') # TELEGRAM_BOT_TOKEN


def on(bot,update):
    chat_id=update.message.chat_id
    bot.send_photo(chat_id,photo='https://cdn1.vectorstock.com/i/1000x1000/59/15/bulb-light-icon-line-lamp-on-symbol-vector-21085915.jpg')
    bot.send_message(chat_id,text='bulb turned on')
    aio = Client(x,y)
    value=Data(value=1)
    value_send=aio.create_data('lightningbot',value)

def off(bot,update):
    chat_id=update.message.chat_id
    bot.send_photo(chat_id,photo='https://cdn5.vectorstock.com/i/1000x1000/59/14/bulb-light-icon-line-idea-symbol-vector-21085914.jpg')
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
