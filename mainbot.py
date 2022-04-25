import logging
from glob import glob
from random import choice, shuffle
import aiogram.dispatcher.webhook
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
import config
from parsing import parsing_info, all_characters
from SQLighter import read_sqlite_table

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    await message.answer("Привет. Это бот по новелле Благословение Небожителей. Чтобы начать, напиши /button")


@dp.message_handler(commands="test4")
async def with_hidden_link(message: types.Message):
    a = parsing_info()
    await message.answer(
        f"{fmt.hide_link(a[0])}{a[1]}",
        parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands="button")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/picture", "/game", "/wiki"]
    keyboard.add(*buttons)
    await message.answer("Выберите, что вам надо", reply_markup=keyboard)


@dp.message_handler(commands='picture')
async def cmd_picture(message: types.Message):
    lists = glob('images_random/*')
    picture = choice(lists)
    photo = open(picture, 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message_handler(commands='game')
async def cmd_game(message: types.Message):
    generate_markup()
    await bot.send_photo(chat_id=message.chat.id, photo=raw[1])
    await message.answer("Выберите правильный ответ", reply_markup=markup)


@dp.message_handler(commands='wiki')
async def cmd_wiki(message: types.Message):
    generate_markup_of_characters()
    await message.answer('Про какого персогажа вы хотите узнать?', reply_markup=markup)


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



# Хэндлер на команду /test2
# async def cmd_test2(message: types.Message):
# await message.reply("Test 2")

# dp.register_message_handler(cmd_test2, commands="test2")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
