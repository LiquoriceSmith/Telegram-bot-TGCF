import telebot
import config
import random
from telebot import types
from glob import glob
from random import choice, shuffle
from SQLighter import read_sqlite_table
from parsing import parsing_info, make_photo_exist, all_characters

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет. Это бот по новелле Благословение Небожителей. "
                                      "Чтобы начать, напиши /button")


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Отправь картинку")
    item2 = types.KeyboardButton("/game")
    item3 = types.KeyboardButton("/Wiki")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(commands=['game'])
def game(message):
    generate_markup()
    bot.send_photo(message.chat.id, raw[1])
    msg = bot.send_message(message.chat.id, 'Выберите верный ответ', reply_markup=markup)
    bot.register_next_step_handler(msg, answer_check)


def answer_check(message):
    if message.text == answer:
        msg = bot.send_message(message.chat.id, 'Верно!')
    if message.text != answer:
        msg = bot.send_message(message.chat.id, 'Вы ошиблись :( Верный ответ: ' + answer)


#   bot.register_next_step_handler(msg, start_message)


# info = parsing_info()[1]
# print(info)


@bot.message_handler(commands=['Wiki'])
def parsing_info(message):
    generate_markup_of_characters()
    msg = bot.send_message(message.chat.id, 'Про какого персонажа вы хотите узнать', reply_markup=markup)
    bot.register_next_step_handler(msg, answer_wiki)


def answer_wiki(message):
    global who
    who = list_of_ch[message.text]


#  bot.send_photo(message.chat.id, photo=open('images_parsing/Хуа_Чэн.jpg', 'rb'))
# bot.send_message(message.chat.id, info)


# _________________________________________-

def generate_markup():
    global markup, raw, answer
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    raw = read_sqlite_table()
    print(raw)
    all_answers = raw[2] + ', ' + raw[3]
    all_answers = all_answers.split(', ')
    answer = raw[2]
    shuffle(all_answers)
    for item in all_answers:
        markup.add(item)
    return markup


def generate_markup_of_characters():
    global markup, list_of_ch
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    list_of_ch = all_characters()
    for key in list_of_ch:
        markup.add(key)
    return markup


@bot.message_handler(content_types='text')
def bot_work(message):
    if message.text == "Отправь картинку":
        lists = glob('images_random/*')
        picture = choice(lists)
        bot.send_photo(message.chat.id, photo=open(picture, 'rb'))


if __name__ == '__main__':
    bot.polling()
# bot.infinity_polling()
