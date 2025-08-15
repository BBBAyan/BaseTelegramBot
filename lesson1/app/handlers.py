from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, callback_query
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.middlewares import TestMiddleware

router = Router()

router.message.outer_middleware(TestMiddleware())

class Reg(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}', reply_markup = kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Команда /help.')

@router.message(F.text == 'Как дела?')
async def msg_how_are_you(message: Message):
    await message.answer('Все хорошо.')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')

@router.message(Command('get_photo'))
async def send_photo(message: Message):
    await message.answer_photo(photo = 'AgACAgIAAxkBAAMhaJwxhkCm3sU-vjAzO-e0PvlWRkEAAvn0MRuoLuFID4FAMFukvhYBAAMCAAN5AAM2BA', caption = 'Список формул')

@router.callback_query(F.data == 'catalog')
async def catalog_callback_query(callback: callback_query):
    await callback.answer('Вы перешли в каталог.', show_alert = True)
    await callback.message.edit_text('Вот каталог машин:', reply_markup = await kb.inline_cars())

@router.message(Command('reg'))
async def cmd_reg1(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя:')

@router.message(Reg.name)
async def cmd_reg2(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите ваш номер:')

@router.message(Reg.number)
async def cmd_reg3(message: Message, state: FSMContext):
    await state.update_data(number = message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо за информацию!\nИмя: {data["name"]}\nНомер: {data["number"]}')
    await state.clear()