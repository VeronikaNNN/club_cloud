import logging
import sys
import data

import telebot.apihelper
import telegram
from telegram.ext import Application, MessageHandler, filters
import config
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from text import list1, list2


token = '5657310993:AAFWBcEwH9WOfOvbZJj8i6q-imDnevYAVsU'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
almazi = 0
bot = telegram.Bot(token)
chat_id = bot.get_updates()

logger = logging.getLogger(__name__)
reply_keyboard1 = [['/help', '/story_selection']]
markup1 = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=False)


async def start(update, context):
    # Первое сообщение с приветствием
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я - бот, с помощью которого ты сможешь отдохнуть и почитать истории."
        rf" Если тебе понадобится помощь, напиши мне об этом )", reply_markup=markup1)


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_text("almazi - узнать количество алмазов")


async def almaz(update, context):  # Количество алмазов
    await update.message.reply_html(rf"Ваши алмазы: {almazi}")


reply_keyboard2 = [['/go_out', '/story_selection']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False)


async def go_out(update, context):
    await update.message.reply_text("Как жаль :( Жду Вас в следующий раз")
    sys.exit()


reply_keyboard = [['/gravity_falls', '/horror']]
"""Клавиатура с выбором жанра"""
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def story_selection(update, context):
    await update.message.reply_text("Какую историю предпочитаете?",
                                    reply_markup=markup)


reply_keyboard4 = [['/next']]
markup4 = ReplyKeyboardMarkup(reply_keyboard4, one_time_keyboard=False)


async def gravity_falls(update, context):
    await update.message.reply_html(list1[0], reply_markup=markup4)


reply_keyboard5 = [['/next1']]
markup5 = ReplyKeyboardMarkup(reply_keyboard5, one_time_keyboard=False)


async def next1(update, context):
    await update.message.reply_html(list1[1], reply_markup=markup5)


reply_keyboard6 = [['/next2']]
markup6 = ReplyKeyboardMarkup(reply_keyboard6, one_time_keyboard=False)


async def next2(update, context):
    await update.message.reply_html(list1[2], reply_markup=markup6)


reply_keyboard7 = [['/next3']]
markup7 = ReplyKeyboardMarkup(reply_keyboard7, one_time_keyboard=False)


async def next3(update, context):
    await update.message.reply_html(list1[3], reply_markup=markup7)


reply_keyboard8 = [['/next4']]
markup8 = ReplyKeyboardMarkup(reply_keyboard8, one_time_keyboard=False)


async def next4(update, context):
    await update.message.reply_html(list1[4], reply_markup=markup8)


reply_keyboard9 = [['/next5']]
markup9 = ReplyKeyboardMarkup(reply_keyboard9, one_time_keyboard=False)


async def next5(update, context):
    await update.message.reply_html(list1[5], reply_markup=markup9)


reply_keyboard10 = [['/next6']]
markup10 = ReplyKeyboardMarkup(reply_keyboard10, one_time_keyboard=False)


async def next6(update, context):
    await update.message.reply_html(list1[6], reply_markup=markup10)


reply_keyboard_s1 = [['agree', 'refuse']]  # Первый выбор
markup_s1 = ReplyKeyboardMarkup(reply_keyboard_s1, one_time_keyboard=False)


async def solution1(update, context):
    await update.message.reply_html('Читатель, что делать Дипперу и Мэйбл?', reply_markup=markup_s1)


reply_keyboard_q1 = [['/twelve', '/thirteen',
                     '/fourteen', '/eleven']]  # Первый выбор
markup_q1 = ReplyKeyboardMarkup(reply_keyboard_q1, one_time_keyboard=False)


async def quiz(update, context):
    await update.message.reply_html('Сколько лет было близнецам в начале лета?', reply_markup=markup_q1)


reply_keyboard_0 = [['/lalala']]  # Первый выбор
markup_0 = ReplyKeyboardMarkup(reply_keyboard_0, one_time_keyboard=False)


async def twelve(update, context):
    await update.message.reply_text("Это правильный ответ!", reply_markup=markup_0)


async def echo(update, context):
    await update.message.reply_text(update.message.text)


def main():
    application = Application.builder().token(token).build()
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("story_selection", story_selection))
    application.add_handler(CommandHandler("almaz", almaz))
    application.add_handler(CommandHandler("gravity_falls", gravity_falls), )
    application.add_handler(CommandHandler("next", next1))
    application.add_handler(CommandHandler("next1", next2))
    application.add_handler(CommandHandler("next2", next3))
    application.add_handler(CommandHandler("next3", next4))
    application.add_handler(CommandHandler("next4", next5))
    application.add_handler(CommandHandler("go_out", go_out))
    application.add_handler(CommandHandler("twelve", twelve))
    application.add_handler(CommandHandler("quiz", quiz))
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
