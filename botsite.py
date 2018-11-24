#подключение необходимых библиотек
import telebot
import requests

#идентификаторы бота и вашего с ним чата
token = 'your_bot_token'
your_chat_id = your_chat_id

#функция проверки сайта
def check_200(hostname):
    #создаем экземпляр бота
    bot = telebot.TeleBot(token)
    #делаем запрос к сайту
    r = requests.get(hostname)
    #если что-то не в порядке уведомляем нас об этом средствами бота
    if r.status_code != 200:
        bot.send_message(your_chat_id, hostname + ': ' + str(r.status_code))
    #возвращать нам ничего не обязательно
    pass

#применяем функцию проверки к целевому сайту
check_200("http://webprogramlife.ru")


#подключение необходимой библиотеки
import telebot

#идентификатор бота
token = 'your_bot_token'

bot = telebot.TeleBot(token)

#на каждое ваше сообщение бот ответит идентификатором чата
@bot.message_handler(content_types=["text"])
def say_chat_id(message):
    bot.send_message(message.chat.id, message.chat.id)

#long polling для слушающего бота
if __name__ == "__main__":
    bot.polling(none_stop=True)

