from telegram import Bot

def send_message(chat_id, message):
    bot = Bot(TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=chat_id, text=message)
