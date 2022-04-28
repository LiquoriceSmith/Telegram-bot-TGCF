from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from SQLighter import read_sqlite_table
from random import shuffle
from create_bot import dp, bot


class Game(StatesGroup):
    count = 0
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()


async def cmd_game(message: types.Message):
    generate_markup()
    await bot.send_photo(chat_id=message.chat.id, photo=raw[1])
    await message.answer("Выберите правильный ответ", reply_markup=markup)
    await Game.q1.set()


async def answer_q1(message: types.Message, state: FSMContext):
    await state.update_data(answer1=message.text)
    data = await state.get_data()
    answer1 = data.get('answer1')
    if answer1 == true_answer:
        Game.count += 1
    generate_markup()
    await bot.send_photo(chat_id=message.chat.id, photo=raw[1])
    await message.answer("Выберите правильный ответ", reply_markup=markup)
    await Game.next()


async def answer_q2(message: types.Message, state: FSMContext):
    await state.update_data(answer1=message.text)
    data = await state.get_data()
    answer1 = data.get('answer1')
    if answer1 == true_answer:
        Game.count += 1
    generate_markup()
    await bot.send_photo(chat_id=message.chat.id, photo=raw[1])
    await message.answer("Выберите правильный ответ", reply_markup=markup)
    await Game.next()


async def answer_q3(message: types.Message, state: FSMContext):
    await state.update_data(answer1=message.text)
    data = await state.get_data()
    answer1 = data.get('answer1')
    if answer1 == true_answer:
        Game.count += 1
    generate_markup()
    await bot.send_photo(chat_id=message.chat.id, photo=raw[1])
    await message.answer("Выберите правильный ответ", reply_markup=markup)
    await Game.next()


async def answer_q4(message: types.Message, state: FSMContext):
    await state.update_data(answer1=message.text)
    data = await state.get_data()
    answer1 = data.get('answer1')
    if answer1 == true_answer:
        Game.count += 1
    generate_markup()
    await bot.send_photo(chat_id=message.chat.id, photo=raw[1])
    await message.answer("Выберите правильный ответ", reply_markup=markup)
    await Game.next()


async def answer_q5(message: types.Message, state: FSMContext):
    await state.update_data(answer1=message.text)
    data = await state.get_data()
    answer1 = data.get('answer1')
    if answer1 == true_answer:
        Game.count += 1
    print(Game.count)
    await message.answer("Вы ответили верно на " + str(Game.count) + " вопросов.")
    await state.finish()


def register_handlers_game(dp: Dispatcher):
    dp.register_message_handler(cmd_game, commands=['game'])
    dp.register_message_handler(answer_q1, state=Game.q1)
    dp.register_message_handler(answer_q2, state=Game.q2)
    dp.register_message_handler(answer_q3, state=Game.q3)
    dp.register_message_handler(answer_q4, state=Game.q4)
    dp.register_message_handler(answer_q5, state=Game.q5)


def generate_markup():
    global markup, raw, true_answer
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    raw = read_sqlite_table()
    print(raw)
    all_answers = raw[2] + ', ' + raw[3]
    all_answers = all_answers.split(', ')
    true_answer = raw[2]
    shuffle(all_answers)
    for item in all_answers:
        markup.add(item)
    return markup
