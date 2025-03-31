from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from pyexpat.errors import messages

from states import UserStates

router = Router()

@router.message(F.text.lower() == "скидки", UserStates.user_main_kb)
async def sistem_loyalty(message: Message):
    message.from_user.id
    await message.answer(f"Количество ваших бонусов составляет {loyalty_bonus}")


