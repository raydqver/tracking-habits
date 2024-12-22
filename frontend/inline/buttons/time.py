from .types import Buttons


def get_hours_buttons() -> Buttons:

    return {
        f"{str(hour).zfill(2)}:00": {"callback_data": str(hour)} for hour in range(24)
    }
