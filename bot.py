import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery

from config import BOT_TOKEN, API_ID, API_HASH
from userbot_manager import start_userbot

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

profiles = {}

@dp.message(F.text == "➕ Profil qo‘shish")
async def add_profile(msg: Message):
    await msg.answer("Telefon raqamni yuboring (userbot uchun)")

@dp.message(F.contact)
async def get_phone(msg: Message):
    phone = msg.contact.phone_number

    name = str(msg.from_user.id) + "_" + phone[-4:]

    asyncio.create_task(start_userbot(name, API_ID, API_HASH, phone))

    profiles[name] = phone

    await msg.answer(f"✅ Profil ulandi:\n{name}")

@dp.message()
async def echo(msg: Message):
    await msg.answer("OK")

async def main():
    print("Bot ishga tushdi 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
