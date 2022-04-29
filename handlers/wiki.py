from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from parsing import parsing_info, all_characters
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as fmt
from create_bot import dp, bot
from handlers.common import cmd_start


class Wiki(StatesGroup):
    namechar = State()


async def cmd_wiki(message: types.Message):
    generate_markup_of_characters()
    await message.answer('Про какого персонажа вы хотите узнать?', reply_markup=markup)
    await Wiki.namechar.set()


async def answer_q1(message: types.Message, state: FSMContext):
    is_error = False
    answer = message.text
    await state.update_data(answer1=answer)
    data = await state.get_data()
    answer1 = data.get('answer1')
    # print(list_of_ch[answer1])
    try:
        a = parsing_info(answer1)
    except AttributeError:
        is_error = True
        await message.answer('Выберите имя из списка.', reply_markup=markup)
        await cmd_wiki(message)
    if is_error is False:
        try:
            await message.answer(f"{fmt.hide_link(a[0])}{a[1].replace('<', 'меньше')}", parse_mode=types.ParseMode.HTML)
        except Exception:
            await message.answer('Сервер не может рассказать про него. Попробуйте это позже')

        await cmd_start(message)
        await state.finish()


def register_handlers_wiki(dp: Dispatcher):
    dp.register_message_handler(cmd_wiki, commands=['wiki'])
    dp.register_message_handler(answer_q1, state=Wiki.namechar)


def generate_markup_of_characters():
    global markup, list_of_ch
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    list_of_ch = all_characters()
    for key in list_of_ch:
        markup.add(key)
    return markup
