from telebot import TeleBot
from telebot.types import Message

from api.users.info import get_my_info_by_token
from handlers.default.registration_error import check_registration
from inline.keypads.users import get_control_bot_kb
from utils.refresh_token import get_response_and_refresh_token


def get_my_info(message: Message, bot: TeleBot):
    token = check_registration(message.chat.id, bot)
    if token is None:
        return
    text, is_active = get_response_and_refresh_token(
        telegram_id=message.chat.id, func=get_my_info_by_token, access_token=token
    )
    bot.send_message(
        message.chat.id, text=text, reply_markup=get_control_bot_kb(is_active)
    )


def register_get_my_info(bot: TeleBot):
    bot.register_message_handler(get_my_info, pass_bot=True, commands=["my_info"])