from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from SQLighter import read_sqlite_table
from random import shuffle
from create_bot import dp, bot
from handlers.common import cmd_start


class Game(StatesGroup):  # Создание класса для игры с использованием машины состояний (StatesGroup)
    count_answer = 0
    count_questions = 0
    q1 = State()  # Задается переменная состояние запуска игры


async def cmd_game(message: types.Message):  # Функция, запускающаяся при выборе игры от пользователя
    global thx_next
    thx_next = set()  # Множество вариантов
    generate_markup()  # Создание списка ответов
    while markup in thx_next:  # Если этого персонажа уже показывали
        generate_markup()
    thx_next.add(markup)
    await message.answer('Игра началась. Всего будет 10 вопросов. Чтобы досрочно остановить игру, отправьте /stop')
    await message.answer("Кто это? Выберите правильный ответ", reply_markup=markup)
    await bot.send_photo(chat_id=message.chat.id, photo=raw[1])  # Отправка изображения пользователю
    await Game.q1.set()  # Задается запуск игры


async def answer(message: types.Message, state: FSMContext):  # Функция, запускающаяся при ответе пользователя
    Game.count_questions += 1
    await state.update_data(answer1=message.text)  # Обновление ответа пользователя
    data = await state.get_data()  # Чтение ответа пользователя
    answer1 = data.get('answer1')  # Запись ответа в переменную
    if answer1 == true_answer:  # Проверка ответа
        Game.count_answer += 1
        await message.answer('Правильный ответ! :)')
    else:
        await message.answer('Неправильный ответ :(')

    if Game.count_questions >= 10 or message.text == '/stop':  # Проверка на завершение игры
        await state.finish()  # Состояние игры закончена
        await message.answer('Игра закончена. Вы правильно ответили на ' + str(
            Game.count_answer) + ' из ' + str(Game.count_questions) + ' вопросов')
        Game.count_answer = 0
        Game.count_questions = 0
        await cmd_start(message)  # Вывод меню выбора
    else:
        await Game.q1.set()  # Состояние новый раунд
        generate_markup()  # Генерация списка ответов
        while markup in thx_next:  # Если этого персонажа уже показывали
            generate_markup()
        thx_next.add(markup)
        await message.answer("Кто это? Выберите правильный ответ", reply_markup=markup)
        await bot.send_photo(chat_id=message.chat.id, photo=raw[1])


def register_handlers_game(dp: Dispatcher):  # Регистрация хэндлеров в процесс "Игра"
    dp.register_message_handler(cmd_game, commands=['game'])
    dp.register_message_handler(answer, state=Game.q1)


def generate_markup():  # Функция, формирующая список вариантов ответа
    global markup, raw, true_answer
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)  # Создание пустого списка ответов
    raw = read_sqlite_table()  # Чтение из БД
    all_answers = raw[2] + ', ' + raw[3]  # Добавление в список правильный ответ и неправльные (2 столбца в БД)
    all_answers = all_answers.split(', ')
    true_answer = raw[2]  # Добавление правильного
    shuffle(all_answers)  # Перемешивание ответов
    for item in all_answers:
        markup.add(item)  # Добавление элементов в список ответов
    return markup
