# main.py

from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from config import TELEGRAM_BOT_TOKEN
from bot_commands import start_bot, stop_bot, set_parameters, set_schedule
from scheduling import schedule_bot_run

def main() -> None:
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start_bot))
    application.add_handler(CommandHandler("stop", stop_bot))
    application.add_handler(CommandHandler("setparameters", set_parameters))
    application.add_handler(CommandHandler("setschedule", set_schedule))
    
    # Start the bot and polling
    application.run_polling()

    # Optionally, if scheduling is implemented
    schedule_bot_run()

if __name__ == '__main__':
    main()
