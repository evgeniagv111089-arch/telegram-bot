import telebot
import os

# Получаем токен из переменной окружения (Render так безопаснее)
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! 🤖 Я бот BizOpti, всегда онлайн!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"Вы сказали: {message.text}")

print("Бот запущен...")
bot.polling(non_stop=True)
