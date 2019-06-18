import telebot
import time

bot_token = '881056307:AAEz53DRVvpuk54KtkqMk21N6z_t5oq54Pk'

bot = telebot.TeleBot(token=bot_token)

def findat(text):
	for t in text:
		if t[0] == '@':
			return t

@bot.message_handler(commands = ['start'])
def send_welcome(message):
	bot.reply_to(message, 'Hey Sanju! Epdi iruka?')

@bot.message_handler(commands = ['help'])
def send_welcome(message):
	bot.reply_to(message, 'Help!!')

@bot.message_handler(func = lambda msg:msg.text is not None and '@' in msg.text)
def at_answer(message):
	texts = message.text.split()
	instaid = findat(texts)
	print(instaid)
	bot.reply_to(message, 'https://www.instagram.com/{}'.format(instaid[1:]))


while True:
	try:
		bot.polling()
	except Exception:
		time.sleep(10)

