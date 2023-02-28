from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware


class EnvironmentMiddleware(LifetimeControllerMiddleware):
    """
    Middleware, который обновляет контекст каждого обновления данными из конфигурационного файла.
    """
    skip_patterns = ["error", "update"]

    def __init__(self, **kwargs):
        """
        Инициализирует объект EnvironmentMiddleware.
        :param kwargs: параметры для обновления контекста.
        """
        super().__init__()
        self.kwargs = kwargs

    async def pre_process(self, obj, data, *args):
        """
        Обновляет контекст каждого обновления данными из конфигурационного файла.
        :param obj: объект telegram.ext.callbackcontext.CallbackContext.
        :param data: словарь, содержащий данные контекста.
        :return: None.
        """
        data.update(**self.kwargs)
