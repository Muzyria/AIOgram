
from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    database: str = '1'        # Название базы данных
    db_host: str = '2'        # URL-адрес базы данных
    db_user: str = '3'         # Username пользователя базы данных
    db_password: str = '4'     # Пароль к базе данных


@dataclass
class TgBot:
    token: str = '5'           # Токен для доступа к телеграм-боту
    admin_ids: list[int] = 173901673, 124543434, 143343455  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


n_data = DatabaseConfig()
print(n_data.__dict__)

n_tg_bot = TgBot()
print(n_tg_bot.__dict__)

n_config = Config(
    tg_bot=TgBot(),
    db=DatabaseConfig()
)
print(n_config.__dict__)

