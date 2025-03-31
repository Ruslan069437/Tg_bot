from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    user_main_kb = State()