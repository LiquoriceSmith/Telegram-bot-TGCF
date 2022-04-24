import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
import config
from parsing import parsing_info

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


# Хэндлер на команду /test2
# async def cmd_test2(message: types.Message):
# await message.reply("Test 2")

# dp.register_message_handler(cmd_test2, commands="test2")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
