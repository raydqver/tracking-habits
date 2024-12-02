from telebot import TeleBot
from telebot.types import CallbackQuery

from keyboards.inline.callback.enums import HabitProperties
from keyboards.inline.callback.factories import opportunities_for_change_factory
from keyboards.inline.keypads.time import get_hour_selection_and_back_kb
from states.habits import ChangeHabitStates
from utils.constants import HABITS_KEY, CONTEXT_KEY
from utils.routers_assistants import request_new_property, change_property_by_callback


def request_new_time(callback: CallbackQuery, bot: TeleBot):
    number = int(opportunities_for_change_factory.parse(callback.data)["num_habit"]) - 1
    with bot.retrieve_data(callback.from_user.id, callback.from_user.id) as data:
        last_time = (
            f"{str(data[HABITS_KEY][number - 1]['notification_hour']).zfill(2)}:00"
        )
        data[CONTEXT_KEY] = number

    request_new_property(
        callback=callback,
        bot=bot,
        new_state=ChangeHabitStates.hour,
        message=f"Выберете другое время, вместо {last_time}",
        number=number,
        reply_markup=get_hour_selection_and_back_kb,
    )


def change_time(callback: CallbackQuery, bot: TeleBot):
    with bot.retrieve_data(callback.from_user.id, callback.from_user.id) as data:
        change_property_by_callback(
            callback=callback,
            bot=bot,
            message="Привычка успешно обновлена!",
            new_data={"notification_hour": int(callback.data)},
            data=data,
            number=data[CONTEXT_KEY],
        )


def register_change_time(bot: TeleBot):
    bot.register_callback_query_handler(
        request_new_time,
        pass_bot=True,
        func=None,
        config=opportunities_for_change_factory.filter(
            property=str(HabitProperties.HOUR)
        ),
    )
    bot.register_callback_query_handler(
        change_time, pass_bot=True, func=None, state=ChangeHabitStates.hour
    )