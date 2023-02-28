import typing

from aiogram.dispatcher.filters import BoundFilter

from tgbot.config import Config


class AdminFilter(BoundFilter):
    """
    Фильтр, который проверяет, является ли пользователь администратором бота.
    """
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        """
        Инициализирует объект AdminFilter.
        :param is_admin: является ли пользователь администратором бота.
        """
        self.is_admin = is_admin

    async def check(self, obj):
        """
        Проверяет, является ли пользователь администратором бота.
        :param obj: объект telegram.ext.callbackcontext.CallbackContext.
        :return: bool - True, если пользователь администратор бота, иначе - False.
        """
        if self.is_admin is None:
            return False
        config: Config = obj.bot.get('config')
        return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_admin
