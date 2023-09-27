
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove)
from my_ import my_token

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = my_token()

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Создаем объекты кнопок
button_1 = KeyboardButton(text='Собак 🦮')
button_2 = KeyboardButton(text='Огурцов 🥒')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]], resize_keyboard=True, one_time_keyboard=True)

# Создаем объекты кнопок
button_1 = KeyboardButton(text='Кнопка 1')
button_2 = KeyboardButton(text='Кнопка 2')
button_3 = KeyboardButton(text='Кнопка 3')
button_4 = KeyboardButton(text='Кнопка 4')
button_5 = KeyboardButton(text='Кнопка 5')
button_6 = KeyboardButton(text='Кнопка 6')
button_7 = KeyboardButton(text='Кнопка 7')
button_8 = KeyboardButton(text='Кнопка 8')
button_9 = KeyboardButton(text='Кнопка 9')

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2, button_3],
              [button_4, button_5, button_6],
              [button_7, button_8, button_9]],
    resize_keyboard=True
)



# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Start',
        reply_markup=my_keyboard
    )





if __name__ == '__main__':
    dp.run_polling(bot)
