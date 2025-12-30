import os
import telebot

# Token Environment Variable থেকে নিন
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    image_url = "https://i.ibb.co/XXXXX/welcome.jpg"

    welcome_text = (
        "👋 স্বাগতম!\n\n"
        "🌆 Image City Bot-এ আপনাকে স্বাগতম\n\n"
        "🖼️ এখানে পাবেন:\n"
        "✅ AI Image\n"
        "✅ Prompt\n"
        "✅ Free Resources"
    )

    bot.send_photo(
        chat_id,
        photo=image_url,
        caption=welcome_text,
        parse_mode="Markdown"
    )

bot.infinity_polling()
