from aiogram import executor
from create_bot import dp
from handlers import wiki, game, picture, common

wiki.register_handlers_wiki(dp)
game.register_handlers_game(dp)
picture.register_handlers_pic(dp)
common.register_handlers_comm(dp)

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
