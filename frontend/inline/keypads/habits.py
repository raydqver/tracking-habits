from telebot.types import InlineKeyboardMarkup

from inline.buttons.cancel import get_home_btn
from inline.buttons.habits import (
    get_my_habits_btn,
    get_selection_to_edit_btn,
    get_habit_properties_buttons,
    get_deleting_habit_btn,
    get_statistics_btn,
    get_tagging_buttons,
    get_reason_waiver_btn,
    get_resuming_btn,
    get_habit_details_btn,
)
from inline.callback.constants import BACK_OUTPUT, MENU_OUTPUT
from inline.keypads.general import create_keyboard


def get_back_to_action_kb(number: int) -> InlineKeyboardMarkup:
    return create_keyboard(get_selection_to_edit_btn(number, key=BACK_OUTPUT))


def get_actions_with_habit_kb(number: int) -> InlineKeyboardMarkup:
    return create_keyboard(
        get_statistics_btn(number),
        get_selection_to_edit_btn(number),
        get_deleting_habit_btn(number),
        get_my_habits_btn(),
        get_home_btn(MENU_OUTPUT),
    )


def get_actions_with_completed_habit_kb(number: int) -> InlineKeyboardMarkup:
    return create_keyboard(
        get_my_habits_btn(),
        get_statistics_btn(number),
        get_resuming_btn(number),
        get_deleting_habit_btn(number),
        get_home_btn(MENU_OUTPUT),
    )


def get_back_to_habits_details_and_menu(number: int) -> InlineKeyboardMarkup:
    return create_keyboard(get_my_habits_btn(), get_habit_details_btn(number))


def get_back_to_habits_kb():
    return create_keyboard(get_my_habits_btn())


def get_properties_to_change_kb(number: int, iz_frozen: bool) -> InlineKeyboardMarkup:
    return create_keyboard(
        get_habit_properties_buttons(number, iz_frozen),
        get_habit_details_btn(number),
        get_my_habits_btn(),
        get_home_btn(MENU_OUTPUT),
    )


def get_reason_waiver_kb():
    return create_keyboard(get_reason_waiver_btn())


def get_opportunity_to_mark_habit_kb(habit_id: int, date: str):
    return create_keyboard(
        get_tagging_buttons(habit_id=habit_id, date=date), row_width=2
    )
