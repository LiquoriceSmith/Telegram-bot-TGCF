from aiogram import types, Dispatcher
from create_bot import dp, bot


async def cmd_test1(message: types.Message):
    await message.answer("Привет. Это бот по новелле Благословение Небожителей. Чтобы начать, напиши /button")


async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/picture", "/game", "/wiki"]
    keyboard.add(*buttons)
    await message.answer("Выберите, что вам надо", reply_markup=keyboard)


async def just_message(message: types.Message):
    if message.text == 'Ты лох':
        await message.answer('Сам такой.')
    else:
        await message.answer("Я тебя не понял :(")
    await cmd_start(message)


def register_handlers_comm(dp: Dispatcher):
    dp.register_message_handler(cmd_test1, commands=['start', 'help'])
    dp.register_message_handler(cmd_start, commands=['button'])
    dp.register_message_handler(just_message)
