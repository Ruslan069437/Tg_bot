from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder
def main_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Заказать")
    kb.button(text="Какой уровень лояльности")
    kb.button(text="Меню")
    return kb.as_markup(resize_keyboard=True)