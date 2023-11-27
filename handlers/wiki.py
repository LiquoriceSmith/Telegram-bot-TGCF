from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from parsing import parsing_info, all_characters
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as fmt
from create_bot import dp, bot
from handlers.common import cmd_start


class Wiki(StatesGroup):  # Класс для процесса wiki
    namechar = State()  # Состояние для машины состояний


async def cmd_wiki(message: types.Message):  # Сообщение, которое выводится при запуске процесса
    generate_markup_of_characters()
    await message.answer('Про какого персонажа вы хотите узнать?', reply_markup=markup)
    await Wiki.namechar.set()  # Какого персонажа выбрал пользователь


async def answer_q1(message: types.Message, state: FSMContext):
    is_error = False
    answer = message.text  # Чтение выбора пользователя
    await state.update_data(answer1=answer)  # Обновление машины состояний
    data = await state.get_data()  # Чтение состояния
    answer1 = data.get('answer1')  # Чтение имени из состояний
    try:  # Проверка на корректность ответа пользователя
        a = parsing_info(answer1)
    except AttributeError:
        is_error = True  # Возбуждение ошибки
        await message.answer('Выберите имя из списка.', reply_markup=markup)
        await cmd_wiki(message)
    if is_error is False:  # Если нет ошибки, то вывод информации после парсинга
        try:
            await message.answer(f"{fmt.hide_link(a[0])}{a[1].replace('<', 'меньше')}", parse_mode=types.ParseMode.HTML)
        except Exception:
            await message.answer('Сервер не может рассказать про него. Попробуйте это позже')

        await cmd_start(message)
        await state.finish()


def register_handlers_wiki(dp: Dispatcher):
    dp.register_message_handler(cmd_wiki, commands=['wiki'])
    dp.register_message_handler(answer_q1, state=Wiki.namechar)


def generate_markup_of_characters():  # Генерация списка персонажей
    global markup, list_of_ch
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)  # Создание клавиатуры
    list_of_ch = all_characters()  # Задаем словарь всех персонажей
    for key in list_of_ch:
        markup.add(key)
    return markup
