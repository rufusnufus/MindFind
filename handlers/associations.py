"""This script defines evrything needed for adding associations of the user"""

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot import dp
from db_worker import add_assoc

class AddAssoc(StatesGroup):
    """
    States order of adding association feature
    """
    waiting_for_sticker = State()
    waiting_for_text = State()


@dp.message_handler(commands="add_association", state="*")
async def assoc_step_1(message: types.Message):
    """
    Answers on /add_association command, changes the state of FSM
    """
    await message.answer("Send me a sticker🐣")
    await AddAssoc.waiting_for_sticker.set()


@dp.message_handler(state=AddAssoc.waiting_for_sticker, content_types=types.ContentTypes.STICKER)
async def assoc_step_2(message: types.Message, state: FSMContext):
    """
    Gets the sticker, changes the state of FSM
    """
    await state.update_data(sticker_id=message.sticker.file_id)
    await AddAssoc.next()
    await message.answer("Now send me the association🐥")


@dp.message_handler(state=AddAssoc.waiting_for_text, content_types=types.ContentTypes.TEXT)
async def food_step_3(message: types.Message, state: FSMContext):
    """
    Gets the association, finishes the FSM
    """
    user_data = await state.get_data()
    ans = ("Great! New association is created😸\nDon't waste time. Test it in inline mode😻")
    add_assoc(message.from_user.id, user_data['sticker_id'], message.text.lower())
    await message.answer(ans)
    await state.finish()
