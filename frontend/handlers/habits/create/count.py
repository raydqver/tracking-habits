from telebot import TeleBot
from telebot.types import Message

from keyboards.inline.keypads.cancel import get_cancel_kb
from states.habits import HabitsStates
from utils.constants import NAME_KEY


def request_count(message: Message, bot: TeleBot):
    with bot.retrieve_data(message.chat.id, message.chat.id) as data:
        print("data2", data)
        data[NAME_KEY] = message.text
    bot.send_message(
        message.chat.id,
        "Введите количество дней для отправки напоминаний (психологи рекомендуют 21 день)",
        reply_markup=get_cancel_kb(),
    )
    bot.set_state(
        user_id=message.chat.id, chat_id=message.chat.id, state=HabitsStates.count
    )


def handle_invalid_count(message: Message, bot: TeleBot):
    bot.send_message(
        message.chat.id,
        "Количество дней для отправки должно быть от 1 до 365. Введите число снова.",
        reply_markup=get_cancel_kb(),
    )


def register_get_count(bot: TeleBot):
    bot.register_message_handler(request_count, pass_bot=True, state=HabitsStates.name)
    bot.register_message_handler(
        handle_invalid_count,
        func=lambda msg: (msg.text.isdigit() and int(msg.text) in range(1, 366))
        is False,
        pass_bot=True,
        state=HabitsStates.count,
    )