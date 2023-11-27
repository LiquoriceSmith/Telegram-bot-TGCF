from aiogram import types, Dispatcher  # Импорт необходимых классов из библиотеки


# асинхронная функция -- ее работа может прерываться другой функцией без прекращения работы первой
# await используется внутри асинхронной функции

async def cmd_test1(message: types.Message):  # Функция, срабатывающая при первом запуске бота и /help
    # Отправка сообщения
    await message.answer("Привет. Это бот по новелле Благословение Небожителей. Чтобы начать, напиши /button")


async def cmd_start(message: types.Message):  # Функция, срабатывающая при завершении других процессов бота
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создание клавиатуры кнопок
    buttons = ["/picture", "/game", "/wiki"]  # Создание кнопок
    keyboard.add(*buttons)  # Добавление кнопок в клавиатуру
    await message.answer("Выберите, что вам надо", reply_markup=keyboard)  # Вывод сообщения и клавиатуры


async def just_message(message: types.Message):  # Функция, реагирующая на сообщение вне процесса бота
    if message.text == 'Ты ***':  # Проверка на мат
        await message.answer('Сам такой.')
    else:  # Проверка на любое сообщение вне процесса
        await message.answer("Я тебя не понял :(")
    await cmd_start(message)


def register_handlers_comm(dp: Dispatcher):  # Регистрация хэндлеров на команды от пользователя
    dp.register_message_handler(cmd_test1, commands=['start', 'help'])
    dp.register_message_handler(cmd_start, commands=['button'])
    dp.register_message_handler(just_message)
