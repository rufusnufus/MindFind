from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot import dp

class AddAssoc(StatesGroup):
    """States order of adding association feature"""
    waiting_for_sticker = State()
    waiting_for_text = State()


@dp.message_handler(commands="add_association", state="*")
async def assoc_step_1(message: types.Message):
    await message.answer("Send me a sticker.")
    await AddAssoc.waiting_for_sticker.set()


@dp.message_handler(state=AddAssoc.waiting_for_sticker, content_types=types.ContentTypes.STICKER)
async def assoc_step_2(message: types.Message, state: FSMContext):
    await state.update_data(sticker_id=message.sticker.file_id)
    await AddAssoc.next()
    await message.answer(f"Sticker's ID: <code>{message.sticker.file_id}</code>")
    await message.answer("Now send me the association.")


@dp.message_handler(state=AddAssoc.waiting_for_text, content_types=types.ContentTypes.TEXT)
async def food_step_3(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    ans = (f"Your new associaion:\nSticker ID: <code>{user_data['sticker_id']}</code>\n"
            "Text: {message.text.lower()}\n")
    await message.answer(ans)
    await state.finish()
