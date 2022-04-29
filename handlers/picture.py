from aiogram import types, Dispatcher
from glob import glob
from random import choice
from create_bot import dp, bot


async def cmd_picture(message: types.Message):
    lists = glob('images_random/*')
    picture = choice(lists)
    photo = open(picture, 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите, что вам надо')


def register_handlers_pic(dp: Dispatcher):
    dp.register_message_handler(cmd_picture, commands=['picture'])
