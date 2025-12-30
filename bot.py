from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_USERNAME = os.environ.get("BOT_USERNAME")

async def start(update, context):
    user = update.effective_user
    uname = user.username or user.first_name or "friend"

    text = (
        f"Hi, @{uname}! 👋\n\n"
        "Welcome to TapCoins Bot 🎮\n\n"
        "TapCoins is what you want it to be."
    )

    keyboard = [
        [InlineKeyboardButton("🎮 Enter TapCoins", callback_data="enter")],
        [InlineKeyboardButton(
            "👥 Invite a Friend",
            url=f"https://t.me/share/url?url=https://t.me/{BOT_USERNAME}"
        )]
    ]

    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
