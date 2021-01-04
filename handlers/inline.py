"""Script defines inline handler for searching stickers associated with entered text"""

import hashlib
from aiogram.types import InlineQuery, InlineQueryResultCachedSticker
from bot import dp, bot
from db_worker import find_stickers

@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    """
    Searches for stickers associated with entered text in DB of the user
    Parameter:
        inline_query: query of the user
    Returns:
        Stickers that are associated by user with entered query.
    """
    text = inline_query.query or 'echo'
    text = text.lower()
    stickers = find_stickers(inline_query.from_user.id, text)
    results = []
    for sticker in stickers:
        result_id: str = hashlib.md5(sticker.encode()).hexdigest()
        results.append(InlineQueryResultCachedSticker(
            id=result_id,
            sticker_file_id=sticker
        ))
    await bot.answer_inline_query(inline_query.id, results=results, cache_time=1)
