from dataclasses import dataclass
from environs import Env


# Создаем экземпляр класса Env
env: Env = Env()
print(env.__dict__)


# Добавляем в переменные окружения данные, прочитанные из файла .env
env.read_env()
print(env('BOT_TOKEN'))

