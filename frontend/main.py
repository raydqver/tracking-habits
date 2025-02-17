import logging

import handlers.auth as auth
import handlers.default as default
import handlers.habits as habits
import handlers.users as users
from apscheduler.schedulers.background import BackgroundScheduler
from config import settings
from inline.filters.habits import EditHabitCallbackFilter
from middlewares.handle_errors import HandleErrorsMiddleware
from telebot import TeleBot
from telebot.custom_filters import StateFilter, TextMatchFilter
from telebot.storage import StateRedisStorage
from utils.scheduler.settings import register_tasks


def register_handlers(bot: TeleBot) -> None:
    """
    Регистрирует все обработчики
    :param bot: TeleBot
    """
    default.register_cancel(bot)
    default.register_start(bot)
    default.register_help(bot)
    auth.register_username(bot)
    auth.register_password(bot)
    auth.register_saving_user(bot)
    auth.register_log_in_username(bot)
    auth.register_log_in_password(bot)
    auth.register_log_in(bot)
    auth.register_require_new_password(bot)
    auth.register_save_password(bot)
    auth.register_invalid_password(bot)
    users.register_get_my_info(bot)
    users.register_activate_or_deactivate(bot)
    habits.register_get_name(bot)
    habits.register_get_count(bot)
    habits.register_get_hour(bot)
    habits.register_get_description(bot)
    habits.register_save_habit(bot)
    habits.register_mark_habit(bot)
    habits.register_get_habits(bot)
    habits.register_get_habit_details(bot)
    habits.register_provide_with_choosing(bot)
    habits.register_delete_habit(bot)
    habits.register_change_name(bot)
    habits.register_change_time(bot)
    habits.register_change_frozen(bot)
    habits.register_change_count(bot)
    habits.register_change_description(bot)
    habits.register_resume_habits(bot)
    habits.register_calendar(bot)

    default.register_unrecognized_events(bot)


def main() -> None:
    """
    Запускает бота
    """
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )

    logger.info("start bot")
    redis_storage = StateRedisStorage(host=settings.redis.redis_host)
    bot = TeleBot(
        settings.bot.token,
        state_storage=redis_storage,
        use_class_middlewares=True,
        parse_mode="HTML",
    )
    bot.add_custom_filter(StateFilter(bot))
    bot.setup_middleware(HandleErrorsMiddleware(bot))
    bot.add_custom_filter(EditHabitCallbackFilter())
    bot.add_custom_filter(TextMatchFilter())
    register_handlers(bot)
    scheduler = BackgroundScheduler()
    scheduler.configure(timezone="Europe/Moscow")
    register_tasks(scheduler=scheduler, bot=bot)
    scheduler.start()
    bot.polling()


if __name__ == "__main__":
    main()
