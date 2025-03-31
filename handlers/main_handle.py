from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.all_keyboards import main_keyboard
from states import UserStates

router = Router()


@router.message(Command("start"))       # /start
async def start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if not True:
        await message.answer("Введите имя")
        await state.set_state(UserStates.user_choise_username)

    else:
        await message.answer(
            text="Выберите что хотите сделать.",
            reply_markup=main_keyboard()
        )
        await state.set_state(UserStates.user_main_kb)
@router.message(F.text, UserStates.user_choise_username)
async def start(message:Message, state:FSMContext):
    user_name = message.text
    await state.set_state(UserStates.user_main_kb)
    await message.answer(
        f"Привет{user_name}!\nВыбери любой пункт:",
        reply_markup=main_keyboard()
    )