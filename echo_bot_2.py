import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from my_ import my_token
from aiogram.types import ContentType
from aiogram import F

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = my_token()

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)


# # Этот хэндлер будет срабатывать на отправку боту голосовым сообщением
# async def send_voice_echo(message: Message):
#     print(message)
#     await message.answer_voice(message.voice.file_id)
# Навешиваем декоратор с указанием в качестве фильтра типа контента
@dp.message(F.voice)
async def process_sent_voice(message: Message):
    # Выводим апдейт в терминал
    print(message)
    # Отправляем сообщение в чат, откуда пришло голосовое
    await message.answer(text='Вы прислали голосовое сообщение!')


# Этот хэндлер будет срабатывать на отправку боту стикер
async def send_sticker_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer_sticker(message.sticker.file_id)


@dp.message(F.video_note)
async def process_sent_v(message: Message):
    # Выводим апдейт в терминал
    print(message)
    # Отправляем сообщение в чат, откуда пришло
    await message.answer(text='Вы прислали video_note сообщение!')

# Этот хэндлер будет срабатывать на отправку боту видео
async def send_video_echo(message: Message):
    print(message)
    await message.answer_video(message.video.file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)


# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
# dp.message.register(send_voice_echo, F.content_type == ContentType.VOICE)
dp.message.register(send_sticker_echo, F.content_type == ContentType.STICKER)
dp.message.register(send_video_echo, F.content_type == ContentType.VIDEO)

dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)
