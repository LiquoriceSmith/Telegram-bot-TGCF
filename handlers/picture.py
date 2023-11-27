from aiogram import types, Dispatcher
from glob import glob
from random import choice
from create_bot import dp, bot


async def cmd_picture(message: types.Message):  # Запуск при выборе процесса отправка изображения
    lists = glob('images_random/*')  # glob() используется для поиска всех файлов в папке
    picture = choice(lists)  # Случайный выбор одной картинки из списка
    photo = open(picture, 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите, что вам надо')  # Меню не убирали, так что просто присылаем сообщение


def register_handlers_pic(dp: Dispatcher):  # Регистрируем хэндлеры для процесса
    dp.register_message_handler(cmd_picture, commands=['picture'])
