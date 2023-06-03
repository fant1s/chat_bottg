import sys
import time
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('xxxxx')

@bot.message_handler(commands=['start']) #Начальное сообщение
def start(message):
    bot.send_message(message.chat.id, 'Привет, это тестовый вариант бота, будут косяки - потерпи чуток')
    bot.send_message(message.chat.id, " Чтоб я начал свою работу напиши /help")

@bot.message_handler(commands=['help']) #Кнопки основные
def firstcommand(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add('Наша группа в ВК')
    markup.add('Покажи где находиться главное предприятие лучших мероприятий всея Руси')
    markup.add('Подскажи куда можно сходить')
    bot.send_message(message.chat.id, 'Щас появиться моё меню', reply_markup=markup)
    bot.send_message(message.chat.id, 'Молодец, правильно нажал, жмакай на кнопки и я буду тебе что-нибудь присылать')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Наша группа в ВК':
        bot.send_message(message.chat.id, 'https://vk.com/liga_elb')
    if message.text == 'Покажи где находиться главное предприятие лучших мероприятий всея Руси':
        bot.send_location(message.chat.id, 55.753699,52.019323)
    if message.text == 'Подскажи куда можно сходить':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='Прогуляться и делать прекрасные селфи', callback_data='red1'))
        markup.add(types.InlineKeyboardButton(text='Отлично провести время', callback_data='green1'))
        markup.add(types.InlineKeyboardButton(text='Сходить по магазинам', callback_data='blue1'))
        markup.add(types.InlineKeyboardButton(text='Где-нибудь перевести дух и вкусно поесть', callback_data='pink1'))
        markup.add(types.InlineKeyboardButton(text='Просто полезные места', callback_data='black1'))
        bot.send_message(message.chat.id, 'Итак, выбери куда хочешь сходить', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'red1':
        bot.send_location(callback.message.chat.id, 55.750754,52.023652)
        bot.send_message(callback.message.chat.id, 'Гуляй парк')
        bot.send_location(callback.message.chat.id, 55.746372,52.032426)
        bot.send_message(callback.message.chat.id, 'Городище')
        bot.send_location(callback.message.chat.id, 55.730354,51.963462)
        bot.send_message(callback.message.chat.id, 'Национальный парк Нижняя Кама')
        bot.send_location(callback.message.chat.id, 52.052064,55.753639)
        bot.send_message(callback.message.chat.id, 'Шишкинские пруды')
    if callback.data == 'green1':
        bot.send_location(callback.message.chat.id, 55.752739,52.030782)
        bot.send_message(callback.message.chat.id, 'Пионерский парк')
    if callback.data == 'pink1':
        bot.send_location(callback.message.chat.id, 55.752013,52.017611)
        bot.send_message(callback.message.chat.id, 'Chill out')
    if callback.data == 'black1':
        bot.send_message(callback.message.chat.id, 'У нас в городе есть отличные места где можно погулять')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='Chill Out', callback_data='black2'))
        markup.add(types.InlineKeyboardButton(text='Муравей', callback_data='black3' ))
        bot.send_message(callback.message.chat.id, 'В Елабуге есть: ', reply_markup=markup)
    if callback.data == 'black2':
        bot.send_location(callback.message.chat.id, 55.752013, 52.017611)
    if callback.data == 'black3':
        bot.send_message(callback.message.chat.id, 'Приветик')
    if callback.data == 'blue1':
        bot.send_location(callback.message.chat.id, 55.7520547,51.9116602)



bot.polling(none_stop=True)


