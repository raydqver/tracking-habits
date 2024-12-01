from sqlalchemy.orm import Session

from database.core.db import GetSession
from database.models import User


@GetSession
def update_token_by_id(telegram_id: int, access_token: str, session: Session):
    user = session.get(User, telegram_id)
    user.access_token = access_token
    session.commit()