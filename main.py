import telebot
from config import keys, TOKEN
from extensions import APIException, Get_Price

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message:telebot.types.Message):
    text =('Для начала работы введите команду в формате: \n<имя валюты>\
    < в какую перевести>\
    < количество переводимой валюты>\
    \n Например: доллар рубль 100\
    \n Доступные валюты по команде /values')
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text,key,))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Не верное количество значений.')
        quote, base, amount = values
        total_base = Get_Price.convert(quote,base,amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {base} в {quote} - {total_base}'
        bot.send_message(message.chat.id,text)
bot.polling()



