from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from generate import ai_generate
import keyboards as kb

router = Router()

# Защита от спама

class Gen(StatesGroup):
    wait = State()

# Ответ и открытие меню при вводе "/start"
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Привет', reply_markup=kb.main )



# Ответ при вводе "/help"

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply('Вы нажали на кнопку помощи', reply_markup=kb.help)

# Тест

@router.message(F.text =='Я @')
async def cmd_help(message: Message):
    await message.reply('Ты @')

# Ответ на повторный запрос до получения ответа от ИИ

@router.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer('Подождите ваш запрос генерируется.')

# Запрос к ИИ

@router.message()
async def genereting(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    respons = await ai_generate(message.text)
    await message.answer(respons)
    await state.clear()