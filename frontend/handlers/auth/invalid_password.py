from inline.keypads.cancel import get_cancel_kb
from states.auth import AuthStates, ChangePasswordStates, LogInStates
from telebot import TeleBot
from telebot.types import Message


def handle_invalid_password(message: Message, bot: TeleBot) -> None:
    """
    Обрабатывает случай, если пользователь присылает невалидный пароль
    :param message: Message
    :param bot: TeleBot
    """
    bot.send_message(
        message.chat.id,
        "Пароль может состоять только из английских букв в любом регистре, цифр и символов нижнего подчеркивания (_).\n"
        "Попробуйте снова",
        reply_markup=get_cancel_kb(),
    )


def register_invalid_password(bot: TeleBot) -> None:
    """
    Регистрирует handle_invalid_password при вводе пароля во время регистрации,
    входе в другой аккаунт и смене пароля
    :param bot: TeleBot
    """
    bot.register_message_handler(
        handle_invalid_password, pass_bot=True, state=AuthStates.password
    )
    bot.register_message_handler(
        handle_invalid_password, pass_bot=True, state=LogInStates.password
    )
    bot.register_message_handler(
        handle_invalid_password, pass_bot=True, state=ChangePasswordStates.password
    )
