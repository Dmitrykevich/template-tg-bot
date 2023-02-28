from aiogram import Dispatcher
from aiogram.types import Message


async def admin_start(message: Message):
    """
    Обрабатывает команду /start от администратора бота.
    :param message: объект telegram.Message.
    :return: None.
    """
    await message.reply("Hello, admin!")


def register_admin(dp: Dispatcher):
    """
    Регистрирует обработчик команды /start для администратора бота.
    :param dp: объект telegram.ext.Dispatcher.
    :return: None.
    """
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
