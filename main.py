import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
TOKEN=os.getenv("BOT_TOKEN")
async def start(update,context):
 kb=[[InlineKeyboardButton("🔴 Live Odds",callback_data="live")]]
 await update.message.reply_text("✅ Bot LIVE!",reply_markup=InlineKeyboardMarkup(kb))
async def live(update,context):
 txt="🔴 LIVE: Sevilla vs Osasuna 1-1 @1.85"
 kb=[[InlineKeyboardButton("Bet @1.85",callback_data="bet")]]
 await update.message.reply_text(txt,reply_markup=InlineKeyboardMarkup(kb))
async def bet(update,context):
 q=update.callback_query
 await q.answer()
 await q.edit_message_text("✅ BET PLACED!")
def main():
 app=Application.builder().token(TOKEN).build()
 app.add_handler(CommandHandler("start",start))
 app.add_handler(CommandHandler("live",live))
 app.add_handler(CallbackQueryHandler(bet))
 app.run_polling()
if __name__=="__main__":
 main()
