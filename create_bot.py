import logging  # для настройки логгирования, которое поможет в отладке
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # хранилища данных для состояний пользователей
import config

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)  # Создание бота с определенным токеном
# Параметр parse_mode отвечает за разметку сообщений. HTML чтобы избежать проблемы с экранированием символов
storage = MemoryStorage()  # Все данные, что не сохранены в БД удалятся.
dp = Dispatcher(bot, storage=storage)  # Соаздение объекта диспетчер
logging.basicConfig(level=logging.INFO)  # Логирование
