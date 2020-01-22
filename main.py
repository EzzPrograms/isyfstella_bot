import telegram
import os
import logging
import time
from functools import wraps
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
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

# Start message
@send_typing_action
def start(update, context):
  time.sleep(0.5)
  context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm Stella.\n"
  "You might know me from ISYF!\n\n"
  "Do /help to see all the commands that I can do!\n")
  pass

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Media
@send_typing_action
def photos(update, context):
  button_list = [
    InlineKeyboardButton("Day 0", url="http://tinyurl.com/isyf2020photosday0"),
    InlineKeyboardButton("Day 1", url="http://tinyurl.com/isyf2020photosday1"),
    InlineKeyboardButton("Day 2", url="http://tinyurl.com/isyf2020photosday2"),
    InlineKeyboardButton("Day 3", url="http://tinyurl.com/isyf2020photosday3"),
    InlineKeyboardButton("Day 4", url="http://tinyurl.com/isyf2020photosday4"),
    InlineKeyboardButton("Day 5", url="http://tinyurl.com/isyf2020photosday5")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
  time.sleep(0.5)
  context.bot.send_message(chat_id=update.effective_chat.id, text="These are the photos from ISYF 2020!", reply_markup=reply_markup)
  pass

photos_handler = CommandHandler('photos', photos)
dispatcher.add_handler(photos_handler)

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
def helpmsg(update, context):
  time.sleep(0.5)
  context.bot.send_message(chat_id=update.effective_chat.id, text="Commands:\n\n"
  "/start: Brings up this welcome message!\n"
  "/photos: Gives direct links to all the ISYF 2020 photos!\n"
  "/videos: Gives links to all the videos from ISYF 2020!\n"
  "/nigel: Soon.\n"
  "/ryan: Does the most basic thing ever.\n"
  "/greenballs: GREEN BALLS\n"
  "/help: Gives a list of all available commands.")
  pass

help_handler = CommandHandler('help', helpmsg)
dispatcher.add_handler(help_handler)

# Group Descriptions
@send_typing_action
def grouplist(update, context):
  button_list = [
    InlineKeyboardButton("Apollo", callback_data="apollo"),
    InlineKeyboardButton("Cassini", callback_data="cassini"),
    InlineKeyboardButton("Curiosity", callback_data="curiosity"),
    InlineKeyboardButton("Discovery", callback_data="stellagang"),
    InlineKeyboardButton("New Horizons", callback_data="nhorizons"),
    InlineKeyboardButton("Parker", callback_data="parker"),
    InlineKeyboardButton("Rosetta", callback_data="rosetta"),
    InlineKeyboardButton("Sputnik", callback_data="sputnik"),
    InlineKeyboardButton("Viking", callback_data="viking"),
    InlineKeyboardButton("Voyager", callback_data="voyager")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))

  context.bot.send_message(chat_id=update.effective_chat.id, text="Which group do you want to know about?", reply_markup=reply_markup)
  pass

def glcallback(update, context):
  button_list = [
    InlineKeyboardButton("Apollo", callback_data="apollo"),
    InlineKeyboardButton("Cassini", callback_data="cassini"),
    InlineKeyboardButton("Curiosity", callback_data="curiosity"),
    InlineKeyboardButton("Discovery", callback_data="stellagang"),
    InlineKeyboardButton("New Horizons", callback_data="nhorizons"),
    InlineKeyboardButton("Parker", callback_data="parker"),
    InlineKeyboardButton("Rosetta", callback_data="rosetta"),
    InlineKeyboardButton("Sputnik", callback_data="sputnik"),
    InlineKeyboardButton("Viking", callback_data="viking"),
    InlineKeyboardButton("Voyager", callback_data="voyager")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))

  query = update.callback_query

  context.bot.edit_message_text(
    chat_id=query.message.chat_id,
    message_id=query.message.message_id,
    text="Which group do you want to know about?",
    reply_markup=reply_markup
  ) 
  
def apollo(update, context):
  query = update.callback_query
  button_list = [
    InlineKeyboardButton("", callback_data="")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))



def cassini(update, context):
  query = update.callback_query
  button_list = [
    InlineKeyboardButton("", callback_data="")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
  
def curiosity(update, context):
  query = update.callback_query
  button_list = [
    InlineKeyboardButton("", callback_data="")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
  
def discovery(update, context):
  query = update.callback_query
  button_list = [
    InlineKeyboardButton("Facilitators List", callback_data="sgfacil"),
    InlineKeyboardButton("Delegates List", callback_data="sgdel"),
    InlineKeyboardButton("Back", callback_data="GroupBack")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))

  time.sleep(0.5)
  context.bot.edit_message_text(
    chat_id=query.message.chat_id,
    message_id=query.message.message_id,
    text="Discovery is part of NASA's space shuttle program and flew more flights than any other Orbital Shuttle.\n"
    "Discovery was a key part of the assembly of the ISS and carried the Hubble Space Telescope into orbit, allowing humans to probe further into the depths of the universe!",
    reply_markup=reply_markup
  )

def discovery_members(update, context):
  query = update.callback_query
  button_list = [
    InlineKeyboardButton("Back", callback_data="stellagang")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))

  time.sleep(0.5)
  if query.data == "sgfacil":
    context.bot.edit_message_text(
      chat_id=query.message.chat_id,
      message_id=query.message.message_id,
      text="Discovery Facilitators:\n\n"
      "1. Nigel\n"
      "2. Yujia\n"
      "3. Loh Yun\n"
      "4. Chuhao",
      reply_markup=reply_markup
    )
  elif query.data == "sgdel":
    context.bot.edit_message_text(
      chat_id=query.message.chat_id,
      message_id=query.message.message_id,
      text="Discovery Delegates:\n\n"
      "1. Emeirul Ezzuddean\n"
      "2. Li Linyu\n"
      "3. Marcin Bartoszewicz\n"
      "4. Sharifah Yura Mona Mas Rahayu\n"
      "5. Aditya Khandelwal\n"
      "6. Hu Man Mak (Emily)\n"
      "7. Hu Tongyu\n"
      "8. Huang Junwei\n"
      "9. Ryan Ng\n"
      "10. Wong Yin Leng Angelina\n"
      "11. Yap Seng Meng Izo\n"
      "12. Zhang Minyue\n",
      reply_markup=reply_markup
    )
  else:
    pass
  
def nhorizons(update, context):
  query = update.callback_query
  
  button_list = [
    InlineKeyboardButton("", callback_data="")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
  
def parker(update, context):
  query = update.callback_query
  button_list = [
    InlineKeyboardButton("", callback_data="")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
  
def rosetta(update, context):
  query = update.callback_query
  button_list = [
    InlineKeyboardButton("", callback_data="")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
  
def sputnik(update, context):
  query = update.callback_query
  button_list = [
    InlineKeyboardButton("", callback_data="")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
  
def viking(update, context):
  query = update.callback_query
  button_list = [
    InlineKeyboardButton("", callback_data="")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
  
def voyager(update, context):
  query = update.callback_query
  button_list = [
    InlineKeyboardButton("", callback_data="")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))

grouplist_handler = CommandHandler('groups', grouplist)
glcallback_handler = CallbackQueryHandler(glcallback, pattern='GroupBack')
dispatcher.add_handler(grouplist_handler)
dispatcher.add_handler(glcallback_handler)

discovery_handler = CallbackQueryHandler(discovery, pattern='stellagang')
dispatcher.add_handler(discovery_handler)

# Miscellaneous Commands
@send_typing_action
def ryan(update, context):
  time.sleep(0.5)
  context.bot.send_message(chat_id=update.effective_chat.id, text="Hello World!")
  pass

ryan_handler = CommandHandler('ryan', ryan)
dispatcher.add_handler(ryan_handler)

@send_typing_action
def nigel(update, context):
  time.sleep(0.5)
  context.bot.send_message(chat_id=update.effective_chat.id, text="Something will be here.\n"
  "Soon.")
  context.bot.send_message(chat_id=update.effective_user.id, text="Watch the rise of a new religion.")
  pass

nigel_handler = CommandHandler('nigel', nigel)
dispatcher.add_handler(nigel_handler)

@send_typing_action
def greenballs(update, context):
  time.sleep(0.5)
  context.bot.send_message(chat_id=update.effective_chat.id, text="All my life, I wanted...")
  
  button_list = [
    InlineKeyboardButton("Full Story Here", callback_data="GBFullStory")
  ]

  reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
  time.sleep(0.5)
  context.bot.send_message(chat_id=update.effective_chat.id, text="*GREEN BALLS*", parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=reply_markup)
  pass
  
gb_handler = CommandHandler('greenballs', greenballs)
dispatcher.add_handler(gb_handler)

@send_typing_action
def gbfull(update, context):
  query = update.callback_query
  context.bot.edit_message_text(
    chat_id=query.message.chat_id,
    message_id=query.message.message_id,
    text="*GREEN BALLS*",
    parse_mode=telegram.ParseMode.MARKDOWN
  )
  time.sleep(0.7)
  context.bot.send_message(chat_id=update.effective_chat.id, text="Green Balls Full Story", reply_to_message_id=query.message.message_id)
  time.sleep(1)
  context.bot.send_message(chat_id=update.effective_chat.id, text="A long long time ago, in a land far far away, there was this young boy. He was talented and excelled at everything he did, often scoring extremely well for his tests.")
  time.sleep(0.7)
  context.bot.send_message(chat_id=update.effective_chat.id, text="Once he got 100/100 for a Math test and his teacher wanted to reward him. So they asked him, “What do you want as a reward?” And he answered, “I want green balls.” His teacher were perplexed and asked him why but he refused to answer.")
  time.sleep(0.7)
  context.bot.send_message(chat_id=update.effective_chat.id, text="Many years later, when he won the Nobel Prize for curing cancer, he declined the Nobel Committee’s prize money. The Committee then asked him what he wanted instead. And he answered, “I want green balls.” The Nobel Committee was perplexed and asked him why but he refused to answer.")
  time.sleep(0.7)
  context.bot.send_message(chat_id=update.effective_chat.id, text="Many years after that, on his deathbed, he gathered all those around him and asked them, “Do you want to know why all my life, I’m been so interested in green balls?” And of course they all said yes. And so he said,")
  time.sleep(0.7)
  context.bot.send_message(chat_id=update.effective_chat.id, text="“I…I…have…”")
  time.sleep(1)
  context.bot.send_message(chat_id=update.effective_chat.id, text="And then he died.")
  pass

gbfull_handler= CallbackQueryHandler(gbfull, pattern="GBFullStory") 
dispatcher.add_handler(gbfull_handler)

@send_typing_action
def unknown(update, context):
  time.sleep(0.5)
  context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=open("images/StellaHappy.webp", 'rb'))
  context.bot.send_message(chat_id=update.effective_chat.id, text="Hmm, this is an invalid command.\n"
  "Try using /help to see all my valid commands!")
  pass

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()