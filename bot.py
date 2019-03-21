import telebot
import requests
import config

from telebot import apihelper

# proxies = {
#   'http': 'http://10.10.1.10:3128',
#   #'https': 'https://222.165.249.43:23500',
#   'https': 'https://45.125.61.209:32804',
# }

#token = '731742271:AAEZy417zuGC8jOOLLts7JBBqx_8Pio-mBg'
#url = 'https://api.telegram.org/bot731742271:AAEZy417zuGC8jOOLLts7JBBqx_8Pio-mBg'
#s = requests.session()
#s.proxies = proxies
#r = s.get('https://api.telegram.org/bot731742271:AAEZy417zuGC8jOOLLts7JBBqx_8Pio-mBg/getUpdates')
#apihelper.proxy = {'https':'socks5://login:pass@12.11.22.33:8000'}
#print(r.json())

bot = telebot.TeleBot(config.token)



@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)