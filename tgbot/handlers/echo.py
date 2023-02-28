from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode


async def bot_echo(message: types.Message):
    """
    Отправляет сообщение с эхом без состояния.
    :param message: объект telegram.Message.
    :return: None.
    """
    text = [
        "Эхо без состояния.",
        "Сообщение:",
        message.text
    ]

    await message.answer('\n'.join(text))


async def bot_echo_all(message: types.Message, state: FSMContext):
    """
    Отправляет сообщение с эхом в состоянии.
    :param message: объект telegram.Message.
    :param state: объект telegram.ext.FSMContext.
    :return: None.
    """
    state_name = await state.get_state()
    text = [
        f'Эхо в состоянии {hcode(state_name)}',
        'Содержание сообщения:',
        hcode(message.text)
    ]
    await message.answer('\n'.join(text))


def register_echo(dp: Dispatcher):
    """
    Регистрирует обработчики сообщений с эхом.
    :param dp: объект telegram.ext.Dispatcher.
    :return: None.
    """
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)
