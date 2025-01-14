import telebot
from telebot import types
import requests
import json
bot = telebot.TeleBot('7781689277:AAFpqS8n29yGU0Ba3Q_PkoUqpgqoIlpoF-0')

API = '9b0628ffceff62581d028da4b2b70bce'


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Соц сети разработчика', url='https://vk.com/lsuperjabickl'))
    bot.send_message(message.chat.id, f'<b>Доброго времени суток, {message.from_user.first_name}! Используй команду /weather для того, чтобы узнать погоду</b>', parse_mode='html',reply_markup=markup)

@bot.message_handler(commands=['weather'])
def main(message):
    bot.send_message(message.chat.id, '<em>Введи название города</em>', parse_mode='html')
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower().replace(" ", "+")
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    bot.reply_to(message, f'Сейчас погода в {city}: {data["main"]["temp"]}° ощущается как: {data["main"]["feels_like"]}°')

bot.polling(non_stop=True)
