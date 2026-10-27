import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot LIVE! I dey online now!")

async def live(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 LIVE: Sevilla vs Osasuna - Bet @1.89")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("live", live))
    app.run_polling()

if __name__ == "__main__":
    main()
