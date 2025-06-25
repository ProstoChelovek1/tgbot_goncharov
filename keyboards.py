from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Кнопки меню

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/start')],
                                     [KeyboardButton(text='/help')]],
                                     resize_keyboard=True, input_field_placeholder="Выберите пункт меню")

# Кнопка в сообщении

help = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Напишите администратуру', callback_data='Help', url='https://t.me/Sasha_113')]
    ]
)