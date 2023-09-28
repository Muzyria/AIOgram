
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButtonPollType,
                           WebAppInfo)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from my_ import my_token

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = my_token()

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# # Инициализируем билдер
# kb_builder = ReplyKeyboardBuilder()
#
# # Создаем кнопки
# contact_btn = KeyboardButton(
#     text='Отправить телефон',
#     request_contact=True
# )
# geo_btn = KeyboardButton(
#     text='Отправить геолокацию',
#     request_location=True
# )
# poll_btn = KeyboardButton(
#     text='Создать опрос/викторину',
#     request_poll=KeyboardButtonPollType()
# )
#
# # Добавляем кнопки в билдер
# kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)
#
# # Создаем объект клавиатуры
# keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
#     resize_keyboard=True,
#     one_time_keyboard=True
# )


# Создаем кнопку
web_app_btn = KeyboardButton(
    text='Start Web App',
    web_app=WebAppInfo(url="https://stepik.org/")
)
# Создаем объект клавиатуры
web_app_keyboard = ReplyKeyboardMarkup(
    keyboard=[[web_app_btn]],
    resize_keyboard=True
)


# Этот хэндлер будет срабатывать на команду "/web_app"
@dp.message(Command(commands='web_app'))
async def process_web_app_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=web_app_keyboard
    )


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        # reply_markup=keyboard
    )




if __name__ == '__main__':
    dp.run_polling(bot)
