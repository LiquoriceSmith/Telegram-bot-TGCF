from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='5154606176:AAGQpKYFccgOrVC7zv7Swo7FU4XFV5aevX4', parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()


@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    await message.answer("Привет.")


@dp.message_handler(Command('test'), state=None)
async def enter_test(message: types.Message):
    await message.answer('Тут я спрошу кого ты хочешь')
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    data = await state.get_data()
    answer1 = data.get('answer1')
    print(answer1)
    await state.finish()


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
