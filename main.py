# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import telebot
from telebot import types
import random
from telegram.ext.dispatcher import run_async
import os

bot = telebot.TeleBot('5234672857:AAFBcclG0PjrDKM-JSPNns3mXlYYHb8Hh84')
"""
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Держи свою валентинку )')
"""
@run_async
@bot.message_handler(commands=["start"])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Треш-валентинка")
    markup.add(item1)
    item2 = types.KeyboardButton("Классическая валентинка")
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

@run_async
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Классическая валентинка":
        ch = random.randint(1,32)
        path = os.getcwd()+'\Норм'+f'\{ch}.jpg'
        photo = open(path, 'rb')
        bot.send_photo(message.chat.id, photo)


    if message.text=="Треш-валентинка":
        ch = random.randint(1,34)
        path = os.getcwd()+'\Треш'+f'\{ch}.jpg'
        photo = open(path, 'rb')
        bot.send_photo(message.chat.id, photo)


bot.polling(none_stop=True, interval=0)


