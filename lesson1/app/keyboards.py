from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Каталог', callback_data = 'catalog')],
    [InlineKeyboardButton(text = 'Корзина', callback_data = 'basket')],
    [InlineKeyboardButton(text = 'Контакты', callback_data = 'contacts')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')

settings = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Youtube', url = 'https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4')],
    [InlineKeyboardButton(text = 'GitHub', url = 'https://github.com/BBBAyan')]
],row_width=1)

cars = ['BMW', 'Tesla', 'Mercedes']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text = car, url = 'https://www.youtube.com/watch?v=qRyshRUA0xM'))
    return keyboard.adjust(2).as_markup()