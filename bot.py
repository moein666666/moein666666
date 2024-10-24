from telebot import TeleBot
from telebot.types import (Message, InlineKeyboardMarkup,
                           InlineKeyboardButton, WebAppInfo)


gfhj

@bot.message_handler(commands=['start'])
def start(message: Message):
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Ton Spiner',
                              web_app=WebAppInfo(
                                  'https://github.com/moein666666/moein666666.git'
                              ))]
    ])

    bot.send_message(chat_id=message.chat.id, text='Hi dear to spin wheel start bot:', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(skip_pending=True)
