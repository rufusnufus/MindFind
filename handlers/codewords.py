"""This script defines evrything needed for adding associations of the user"""

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot import dp, codeword_kb
from db_worker import add_codeword, find_codewords


class AddCodeword(StatesGroup):
    """
    States order of adding codeword feature
    """
    waiting_for_sticker = State()
    waiting_for_text = State()


@dp.message_handler(commands="add_codeword", state="*")
@dp.message_handler(Text(equals="Add codeword 😉", ignore_case=False), state="*")
async def codeword_step_1(message: types.Message):
    """
    Answers on /add_codeword command, changes the state of FSM
    """
    await message.answer("Send me a sticker", reply_markup=types.ReplyKeyboardRemove())
    await AddCodeword.waiting_for_sticker.set()


@dp.message_handler(state=AddCodeword.waiting_for_sticker, content_types=types.ContentTypes.STICKER)
async def assoc_step_2(message: types.Message, state: FSMContext):
    """
    Gets the sticker, changes the state of FSM
    """
    await state.update_data(sticker_id=message.sticker.file_id)
    await AddCodeword.next()
    await message.answer("Now send me the codeword")


@dp.message_handler(state=AddCodeword.waiting_for_text, content_types=types.ContentTypes.TEXT)
async def food_step_3(message: types.Message, state: FSMContext):
    """
    Gets the codeword, finishes the FSM
    """
    user_data = await state.get_data()
    ans = ("Great! New codeword is added😸\n"
            "To try it out in any chat you want write:\n"
            f"@MindFindBot {message.text}")
    add_codeword(message.from_user.id, user_data['sticker_id'], message.text.lower())
    await message.answer(ans, reply_markup=codeword_kb)
    await state.finish()


@dp.message_handler(commands="codewords")
async def send_codewords(message: types.Message):
    """
    This handler will be called when user sends `/codewords` command
    """
    codewords = find_codewords(message.from_user.id)
    answer = '\n'.join(codewords)
    await message.reply(answer, reply_markup=codeword_kb)
