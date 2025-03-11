# from transliterate import to_cyrillic, to_latin
# import telebot

# TOKEN = "7995261769:AAHfFMPZeoJtxi7iza6cIODNXxvNnIJjmms"
# bot = telebot.TeleBot(TOKEN, parse_mode=None)

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Assalamu Aleykum, Welcoming! \nEnter a text:")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     mes = message.text
#     response = lambda mes: to_cyrillic(mes) if mes.isascii() else to_latin(mes)
#     bot.reply_to(message, response)


# bot.polling()


# text = input("Enter any text: ")

# if text.isascii():
#     print(to_cyrillic(text))
# else:
#     print(to_latin(text))

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "7995261769:AAHfFMPZeoJtxi7iza6cIODNXxvNnIJjmms"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalamu Aleykum! Matn kiriting:")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    # Lotin yoki Kirill ekanini aniqlash
    if msg == to_cyrillic(to_latin(msg)):
        response = to_latin(msg)  # Kirilldan Lotinga
    else:
        response = to_cyrillic(msg)  # Lotindan Kirillga
    bot.reply_to(message, response)

bot.polling()
