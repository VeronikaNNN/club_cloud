import logging
from telegram.ext import Application, MessageHandler, filters
import config
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup


token = '5657310993:AAFWBcEwH9WOfOvbZJj8i6q-imDnevYAVsU'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def hello(update, context):
    """Первое сообщение с приветствием"""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я - бот, с помощью которого ты сможешь отдохнуть и почитать истории."
        rf" Если тебе понадобится помощь, напиши мне об этом )",
    )


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_text("Я пока не умею помогать.")


reply_keyboard = [['/romance', '/horror']]
"""Клавиатура с выбором жанра"""
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def genre(update, context):
    await update.message.reply_text("Какой жанр вы предпочитаете?",
                                    reply_markup=markup)


async def echo(update, context):
    await update.message.reply_text(update.message.text)


def main():
    application = Application.builder().token(token).build()
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(CommandHandler("hello", hello))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("genre", genre))
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
