import telebot
import requests
import json


bot= telebot.TeleBot('6655403971:AAE_uFh0YKmctklpucG8uTRnGubl5DiSUvg')
API='0fe6e453f3012dd5806bcd3bb3cb1231'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет рад тебя видеть! Напиши название города')
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city=message.text.strip().lower()
    res= requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code==200:
        data=json.loads(res.text)
        bot.reply_to(message,f'Сейчас погода:{data["main"]["temp"]} градусов')
    else:
        bot.reply_to(message, f'Город указан не верно.Напишите  правильно имя вашего города')




bot.polling(none_stop=True)
