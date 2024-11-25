from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from .base import BaseModel


class UserModel(BaseModel):
    username: Mapped[str]
    password: Mapped[bytes]
    telegram_id: Mapped[int] = mapped_column(BigInteger)
    is_active: Mapped[bool] = mapped_column(default=True)
