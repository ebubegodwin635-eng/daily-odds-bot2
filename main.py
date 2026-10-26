import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚽ DAILY SURE 2 ODDS - LIVE\n\n/live - Live matches")

async def live(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = "🔴 LIVE: Sevilla vs Osasuna 1-1 (65')\nOdds:"
    kb = [[InlineKeyboardButton("Sevilla @1.95", callback_data="Sevilla")],[InlineKeyboardButton("Draw @3.30", callback_data="Draw")],[InlineKeyboardButton("Osasuna @3.80", callback_data="Osasuna")]]
    await update.message.reply_text(txt, reply_markup=InlineKeyboardMarkup(kb))

async def bet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    await q.edit_message_text(f"✅ BET PLACED: {q.data}\nTo Win: 1950")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("live", live))
    app.add_handler(CallbackQueryHandler(bet))
    app.run_polling()

if __name__ == "__main__":
    main()
