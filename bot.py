import telebot


api = '8305761739:AAE_A5clB4wingSLkz-15OB-xDDLczP_qrA'

 

bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])

def send_welcome(message):

    bot.reply_to(message, 'WELCOME TO DIKXZ STORE @DIKXZ_STOREE                WEBSITE https://dikxzstore.olshopku.com')

 

print('Bot Running....')

bot.polling(
