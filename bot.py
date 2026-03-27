import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

from config import BOT_TOKEN, ADMIN_ID, CARD, OWNER
import db

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ================= MENU =================
def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📂 Chatlar", callback_data="chats")],
            [InlineKeyboardButton(text="💎 Premium", callback_data="premium")]
        ]
    )

# ================= START =================
@dp.message(CommandStart())
async def start(msg: Message):
    db.add_user(msg.from_user.id)
    await msg.answer("👋 Xush kelibsiz", reply_markup=main_menu())

# ================= PREMIUM =================
@dp.callback_query(F.data == "premium")
async def premium(call: CallbackQuery):
    await call.message.answer(
        f"💳 To‘lov uchun:\n{CARD}\n👤 {OWNER}\n\nChek yuboring"
    )
    await call.answer()

# ================= CHAT BUTTON =================
@dp.callback_query(F.data == "chats")
async def chats(call: CallbackQuery):
    await call.message.answer("📂 Chatlar hali ulanmagan")
    await call.answer()

# ================= CHECK PAYMENT (PHOTO) =================
@dp.message(F.photo)
async def check(msg: Message):
    await bot.send_photo(
        ADMIN_ID,
        msg.photo[-1].file_id,
        caption=f"User: {msg.from_user.id}"
    )

# ================= RUN =================
async def main():
    print("Bot ishga tushdi 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
