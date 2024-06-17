﻿# CurrencyconverterTGBot

 Telegram-бот, с использованием библиотеки pytelegrambotapi в котором будет реализован следующий функционал:

 - Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
 - Пользователь отправляет сообщение боту в виде <имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>.
 - При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
 - При вводе команды /values выводиться информация о всех доступных валютах в читаемом виде.
 - Для получения курса валют необходимо использовать любое удобное API и отправлять к нему запросы с помощью библиотеки Requests.
 - Для парсинга полученных ответов использовать библиотеку JSON.
 - При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число) вызывается собственно написанное исключение APIException с текстом пояснения ошибки.
 - Текст любой ошибки с указанием типа ошибки отправлятся пользователю в сообщения.

 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
In English

Telegram bot, using the pytelegrambotapi library, which will implement the following functionality:

 - The bot returns the price for a certain amount of currency (euro, dollar or ruble).
 - The user sends a message to the bot in the form <name of the currency whose price he wants to know> <name of the currency in which he wants to know the price of the first currency> <amount of the first currency>.
 - When you enter the /start or /help command, the user is given instructions on how to use the bot.
 - When you enter the /values ​​command, information about all available currencies is displayed in readable form.
 - To get the exchange rate, you need to use any convenient API and send requests to it using the Requests library.
 - Use the JSON library to parse received responses.
 - If a user error occurs (for example, an incorrect or non-existent currency was entered, or an incorrect number was entered), a custom APIException is thrown with text explaining the error.
 - The text of any error indicating the type of error will be sent to the user in messages.
