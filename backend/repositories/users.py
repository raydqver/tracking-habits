from sqlalchemy import select, null
from sqlalchemy.ext.asyncio import AsyncSession

from models import UserModel, HabitModel
from repositories.repository import ManagerRepository


class UserRepository(ManagerRepository):
    model = UserModel

    @classmethod
    async def get_users_habits_by_hour(cls, session: AsyncSession, hour: int):
        query = (
            select(cls.model.telegram_id, HabitModel.id, HabitModel.name)
            .join(HabitModel)
            .filter(
                HabitModel.notification_hour == hour,
                cls.model.is_active == True,
                HabitModel.is_frozen == False,
                HabitModel.completed_at == null(),
            )
            .order_by(cls.model.telegram_id)
        )
        result = await session.execute(query)
        return result.all()

    @classmethod
    async def get_user_info(cls, session: AsyncSession, user_id: int):
        query = select(
            cls.model.username, cls.model.is_active, cls.model.date_of_registration
        ).filter_by(id=user_id)
        result = await session.execute(query)
        return result.first()
