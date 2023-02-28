from aiogram import Dispatcher
from aiogram.types import Message


async def user_start(message: Message):
    """
    Обрабатывает команду /start от пользователя бота.
    :param message: объект telegram.Message.
    :return: None.
    """
    await message.reply("Hello, user!")


def register_user(dp: Dispatcher):
    """
    Регистрирует обработчик команды /start для пользователя бота.
    :param dp: объект telegram.ext.Dispatcher.
    :return: None.
    """
    dp.register_message_handler(user_start, commands=["start"], state="*")
