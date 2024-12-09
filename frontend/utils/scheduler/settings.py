from apscheduler.schedulers.background import BackgroundScheduler
from telebot import TeleBot

from .tasks import send_reminders_to_all_users


def register_tasks(scheduler: BackgroundScheduler, bot: TeleBot):
    for hour in range(23):
        scheduler.add_job(
            send_reminders_to_all_users,
            "cron",
            hour=f"{hour}",
            minute="0",
            kwargs={"bot": bot, "hour": hour},
        )
