import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
)

# ==========================================
# SOZLAMALAR
# ==========================================

BOT_TOKEN = os.getenv("BOT_TOKEN")

WEB_APP_URL = (
    "https://raxmonjonov77-hash.github.io/"
    "matematika-milliy-sertifikat/index.html"
)

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN topilmadi!")

# ==========================================
# BOT
# ==========================================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# ==========================================
# START
# ==========================================

@dp.message(CommandStart())
async def start(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 MATHCERT UZ TEST",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )

    await message.answer(
        "🧮 MATHCERT UZ\n\n"
        "Matematika Milliy Sertifikat "
        "mock testlarini ishlang!\n\n"
        "👇 Testni boshlash uchun tugmani bosing:",
        reply_markup=keyboard
    )


# ==========================================
# TEST
# ==========================================

@dp.message(Command("test"))
async def test(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 TESTNI BOSHLASH",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )

    await message.answer(
        "🚀 MATHCERT UZ Mini App",
        reply_markup=keyboard
    )


# ==========================================
# HELP
# ==========================================

@dp.message(Command("help"))
async def help_command(message: Message):

    await message.answer(
        "🧮 MATHCERT UZ\n\n"
        "/start — Botni boshlash\n"
        "/test — Mock testni ochish\n"
        "/help — Yordam"
    )


# ==========================================
# ISHGA TUSHIRISH
# ==========================================

async def main():

    logging.basicConfig(level=logging.INFO)

    print("================================")
    print("MATHCERT UZ BOT ISHLAYAPTI")
    print("WEB APP URL:")
    print(WEB_APP_URL)
    print("================================")

    await dp.start_polling(bot)


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    asyncio.run(main())
