from aiogram import executor
from create_bot import dp
from handlers import wiki, game, picture, common

wiki.register_handlers_wiki(dp)  # подключение хэндлера википедии
game.register_handlers_game(dp)  # подключение хэндлера игры
picture.register_handlers_pic(dp)  # подключение хэндлера картинок
common.register_handlers_comm(dp)  # подключение общего хэндлера

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)  # Запуск бота
