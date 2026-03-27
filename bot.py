from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from config import *
import db

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def main_menu():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("📂 Chatlar", callback_data="chats"))
    kb.add(InlineKeyboardButton("💎 Premium", callback_data="premium"))
    return kb

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    db.add_user(msg.from_user.id)
    await msg.answer("👋 Xush kelibsiz", reply_markup=main_menu())

@dp.callback_query_handler(lambda c: c.data == "premium")
async def premium(call: types.CallbackQuery):
    await call.message.answer(
        f"💳 To‘lov uchun:\n{CARD}\n👤 {OWNER}\n\nChek yuboring"
    )

@dp.message_handler(content_types=['photo'])
async def check(msg: types.Message):
    await bot.send_photo(
        ADMIN_ID,
        msg.photo[-1].file_id,
        caption=f"User: {msg.from_user.id}"
    )

async def main():
    await dp.start_polling()

asyncio.run(main())
