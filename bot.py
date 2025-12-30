import telebot

BOT_TOKEN = "8009276855:AAFcYszwcH6pFKEgUt_dsdbzxx6UTOPxmnc"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(
        message.chat.id,
        "👋 Welcome to Image City Bot 🌆"
    )

bot.infinity_polling()
