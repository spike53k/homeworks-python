import telebot
import datetime as dt

api_token = "8290886497:AAF-KrADQJCtAN9RDmgfLQCJIMhROwCIaWU"

bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "Привет, я бот консультант.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "На какие команды я могу отвечать:\n"
                                      "/start - приветствие\n"
                                      "/help - список команд\n"
                                      "/info - информация о боте\n"
                                      "/date - узнать сегодняшнею дату")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.send_message(message.chat.id, "Я простой бот консультант, напиши /help чтобы узнать о моих командах.")

@bot.message_handler(commands=['date'])
def send_date(message):
    now = dt.datetime.now()
    bot.send_message(message.chat.id, f"Дата: {now.day}.{now.month}.{now.year}")

bot.polling()