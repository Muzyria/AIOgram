from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from my_ import my_token

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = my_token()

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def my_start_filter(message: Message) -> bool:
    return message.text == '/start'


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    print(message.text)
    await message.answer(text='Это команда /start')


if __name__ == '__main__':
    dp.run_polling(bot)
