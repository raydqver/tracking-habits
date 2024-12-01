from sqlalchemy.orm import Session

from database.core.db import GetSession
from database.models import User


@GetSession
def add_new_user(telegram_id: int, access_token: str, session: Session) -> None:
    user = User(telegram_id=telegram_id, access_token=access_token)
    session.add(user)
    session.commit()