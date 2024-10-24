from telebot import TeleBot
from telebot.types import (Message, InlineKeyboardMarkup,
                           InlineKeyboardButton, WebAppInfo)


bot = TeleBot('8078732381:AAGGa4tN4gjBg7VGxpVoBqfkl6oNKAU5TOw')


@bot.message_handler(commands=['start'])
def start(message: Message):
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Ton Spiner',
                              web_app=WebAppInfo(
                                  'https://0058-212-30-36-174.ngrok-free.app'
                              ))]
    ])

    bot.send_message(chat_id=message.chat.id, text='Hi dear to spin wheel start bot:', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(skip_pending=True)
