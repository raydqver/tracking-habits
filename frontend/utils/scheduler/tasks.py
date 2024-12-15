import logging
from concurrent.futures import ThreadPoolExecutor

from telebot import TeleBot
from telebot.apihelper import ApiTelegramException

from api.habits.all_habits import get_habits_all_users_by_hour
from api.users.activity_user import activate_or_deactivate_user_by_flag
from database.crud.check_user import get_user_token
from inline.keypads.habits import get_opportunity_to_mark_habit_kb
from utils.exceptions import InvalidApiResponse
from utils.refresh_token import get_response_and_refresh_token

d = [f"202411{str(k).zfill(2)}" for k in range(1, 30)]

logger = logging.getLogger(__name__)


def deactivate_user(telegram_id: int):
    token = get_user_token(telegram_id=telegram_id)
    get_response_and_refresh_token(
        telegram_id=telegram_id,
        func=activate_or_deactivate_user_by_flag,
        access_token=token,
        is_active=False,
    )


def send_user_notification(bot: TeleBot, habit: dict, current_date: str):
    try:
        bot.send_message(
            chat_id=habit["telegram_id"],
            text=f"Пришло время отчета о привычке: «{habit['name']}».\nПожалуйста, нажмите на кнопку ниже",
            reply_markup=get_opportunity_to_mark_habit_kb(
                habit_id=habit["id"], date=current_date
            ),
        )
    except ApiTelegramException as e:
        logger.error("%s", e.description)
        deactivate_user(habit["telegram_id"])


def send_reminders_to_all_users(bot: TeleBot, hour: int) -> None:
    # current_date = datetime.now().strftime("%Y%m%d")
    current_date = d.pop(0)
    # current_date = "20241214"
    try:
        habits = get_habits_all_users_by_hour(hour=hour)
        with ThreadPoolExecutor(max_workers=10) as executor:
            tasks = [
                executor.submit(
                    send_user_notification,
                    bot=bot,
                    habit=habit,
                    current_date=current_date,
                )
                for habit in habits
            ]
            for task in tasks:
                task.result()
    except InvalidApiResponse as e:
        logger.error("Не удалось получить привычки: %s", str(e))