# bot_commands.py

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def start_bot(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot started!')

def stop_bot(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot stopped!')

def set_parameters(update: Update, context: CallbackContext) -> None:
    # Extract parameters from the message
    # Example: /setparameters 10 150
    try:
        params = context.args
        investment_percentage = int(params[0])
        milestone_percentage = int(params[1])
        # Save parameters or apply them to the bot
        update.message.reply_text(f'Parameters set: Investment {investment_percentage}%, Milestone {milestone_percentage}%')
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /setparameters [investment_percentage] [milestone_percentage]')

def set_schedule(update: Update, context: CallbackContext) -> None:
    # Extract schedule from the message
    # Example: /setschedule 09:00 18:00
    try:
        schedule = context.args
        start_time = schedule[0]
        end_time = schedule[1]
        # Save or apply schedule to the bot
        update.message.reply_text(f'Schedule set: Start at {start_time}, End at {end_time}')
    except IndexError:
        update.message.reply_text('Usage: /setschedule [start_time] [end_time]')
