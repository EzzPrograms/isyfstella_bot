import telegram
import os
import logging
import time
from functools import wraps
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token=os.getenv('SECRETAPI'), use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def send_action(action):
  """Sends `action` while processing func command."""

  def decorator(func):
    @wraps(func)
    def command_func(update, context, *args, **kwargs):
      context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
      return func(update, context,  *args, **kwargs)
    return command_func
    
  return decorator

send_typing_action = send_action(ChatAction.TYPING)

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
  menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
  if header_buttons:
    menu.insert(0, header_buttons)
  if footer_buttons:
    menu.append(footer_buttons)
  return menu

@send_typing_action
def start(update, context):
  time.sleep(0.5)
  context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm Stella.\nYou might know me from ISYF!\n\nHere are the commands that I can do:\n/start: Brings up a welcome message!\n/photos: Gives direct links to all the ISYF 2020 photos!\n/videos: Gives links to all the videos from ISYF 2020!\n/ryan: Does the most basic thing ever.\n/help: Gives a list if all available commands.");
  pass

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

@send_typing_action
def photos(update, context):
  time.sleep(0.5)
  context.bot.send_message(chat_id=update.effective_chat.id, text="Here are the links!\n\nDay 0: http://tinyurl.com/isyf2020photosday0\n\nDay 0.5: http://tinyurl.com/isyf2020photosday1\n\nDay 2: http://tinyurl.com/isyf2020photosday2\n\nDay 3: http://tinyurl.com/isyf2020photosday3\n\nDay 4: http://tinyurl.com/isyf2020photosday4\n\nDay 5: http://tinyurl.com/isyf2020photosday5")
  pass

photos_handler = CommandHandler('photos', photos)
dispatcher.add_handler(photos_handler)

@send_typing_action
def helpmsg(update, context):
  time.sleep(0.5)
  context.bot.send_message(chat_id=update.effective_chat.id, text="Commands:\n\n/start: Brings up this welcome message!\n/photos: Gives direct links to all the ISYF 2020 photos!\n/videos: Gives links to all the videos from ISYF 2020!\n/ryan: Does the most basic thing ever.\n/help: Gives a list of all available commands.")
  pass

help_handler = CommandHandler('help', helpmsg)
dispatcher.add_handler(help_handler)

@send_typing_action
def ryan(update, context):
  time.sleep(0.5)
  context.bot.send_message(chat_id=update.effective_chat.id, text="Hello World!")
  pass

ryan_handler = CommandHandler('ryan', ryan)
dispatcher.add_handler(ryan_handler)

@send_typing_action
def videos(update, context):
  button_list = [
    InlineKeyboardButton("Opening Ceremony", url="https://youtu.be/YbGXT5pI1F4"),
    InlineKeyboardButton("Facilitator Intro", url="https://youtu.be/poOgi4r45fs"),
    InlineKeyboardButton("Closing Ceremony", url="https://youtu.be/ysrZWIcMC6g")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
  time.sleep(0.5)
  context.bot.send_message(chat_id=update.effective_chat.id, text="These are the videos from ISYF 2020!", reply_markup=reply_markup)
  pass

videos_handler = CommandHandler('videos', videos)
dispatcher.add_handler(videos_handler)

@send_typing_action
def unknown(update, context):
  time.sleep(0.5)
  context.bot.send_sticker(chat_id=update.effective_chat.id, sticker="https://github.com/EzzPrograms/Misc-Stuff/blob/master/STK-20200116-WA0049.webp?raw=true")
  context.bot.send_message(chat_id=update.effective_chat.id, text="Hmm, this is an invalid command.\nTry using /help to see all my valid commands!")
  pass

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()