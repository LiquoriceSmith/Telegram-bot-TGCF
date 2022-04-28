from aiogram import types, Dispatcher
from SQLighter import read_sqlite_table
from random import shuffle
from create_bot import dp, bot


async def cmd_game(message: types.Message):
    generate_markup()
    await bot.send_photo(chat_id=message.chat.id, photo=raw[1])
    await message.answer("Выберите правильный ответ", reply_markup=markup)


def register_handlers_game(dp: Dispatcher):
    dp.register_message_handler(cmd_game, commands=['game'])


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
