from telebot import TeleBot

token = "6777147481:AAG5gvw5ob50soagZuesfgn1gAN4k0UOgU4"

bot = TeleBot(token)


@bot.message_handler(content_types=["start"])
def start(massage):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    bot.send_message(chat_id, f"salom {first_name}")