import config
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=config.API_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler()
async def index(message: types.Message):
    await message.answer(f"lol {message.text}")


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
