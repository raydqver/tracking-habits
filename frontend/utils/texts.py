TASK_WAS_NOT_COMPLETED_TEXT: str = (
    "К сожалению, сегодня задача не выполнена😓. Постарайтесь выполнить ее завтра!"
)

COMMANDS: str = (
    "Доступные команды:\n\n"
    "/create_habit - создать новую привычку\n"
    "/my_habits - получить привычки, которые еще действуют или временно приостановлены\n"
    "/completed_habits - получить информацию об уже завершенных привычках\n"
    "/my_info - получить информацию о себе или временно отключить бота\n"
    "/change_password - сменить пароль\n"
    "/help - подробное руководство по использованию бота."
)

DELETE_PASSWORD: str = "❗Пожалуйста, запомните пароль его и удалите из переписки"

HABIT_WAS_CREATED: str = "Привычка успешно добавлена!✅"
MARKED_DATE: str = "🟢"
UNMARKED_DATE: str = "🔴"

ABOUT_BOT: str = (
    "Данный бот позволяет отслеживать прогресс по привычкам, анализировать статистику, а также каждый день отправляет "
    "напоминание в одно и то же время.\n\n"
    "Чтобы пользоваться ботом, нужно лишь ввести юзернейм и пароль. С помощью этих данных можно удобно использовать "
    "один профиль на разных аккаунтах в телеграме. "
    "Помните, что после входа в профиль через другой аккаунт будет осуществлен автоматический выход их предыдущего "
    "аккаунта. Войти снова можно будет также с помощью логина и пароля.\n\n"
    "Общение с ботом происходит с помощью кнопок или команд. Их можно ввести вручную или нажать на подсвеченную "
    "синим цветом надпись, начинающуюся с '/'\n\n"
    "Подробная информация о командах:\n\n"
    "/create_habit - позволяет зарегистрировать новую привычку. Запрашивает название, количество дней, сколько вы "
    "желаете получать уведомления, "
    "время по Москве, необязательное описание.\n"
    "/my_habits - выводит действующие привычки или временно приостановленные. С помощью клавиатуры под текстом можно "
    "удалить привычку совсем, приостановить, "
    "редактировать всю информацию или получить статистику в виде календаря с прогрессом. Нажав на день с "
    "невыполненной задачей можно увидеть причину, если она была задана.\n"
    "/change_password - позволяет сменить пароль. Рекомендуем менять его каждые 3 месяца и делать его как можно "
    "длиннее и сложнее.\n"
    "/my_info - выводит информацию о вашем профиле. Позволяет приостановить бота целиком, в таком случае он не будет присылать "
    "уведомления. Если уведомлений о привычках нет, проверьте статус 'Активен'.\n"
    "/completed_habits - выводит информацию о завершенных привычках. Их можно возобновить, удалить и посмотреть о "
    "них статистику.\n\n"
    "Каждый день бот присылает напоминания о ваших действующих привычках в соответствии с их временем.\n\n"
    "Напоминание представляет из себя выбор действий: отметить привычку как выполненную, невыполненную "
    "(опционально можно указать причину), временно её приостановить.\n\n"
    "Если вы забыли отметить привычку в день напоминания, то можете сделать это позже, нажав на кнопку в день "
    "отправления."
)
