from telebot import TeleBot

token = "6934792957:AAGc3dv5mFQMS8LwaEvboTrUmZwWk-e9YsY"

bot = TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    firstname = message.from_user.first_name
    id = message.from_user.id
    username = message.from_user.username
    bot.send_message(chat_id, f"salom {firstname}\n sizning id: {id}\n foydalanuvchi nomi: {username}")

bot.polling(none_stop=True)