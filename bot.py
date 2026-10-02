import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    WebAppInfo,
    BotCommand,
)

TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN topilmadi")

if not WEB_APP_URL:
    raise RuntimeError("WEB_APP_URL topilmadi")

bot = Bot(token=TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🚀 Testni boshlash",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ],
        [
            KeyboardButton(text="📚 Qoidalar"),
            KeyboardButton(text="⭐ Premium")
        ],
    ],
    resize_keyboard=True,
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🧮 MATHCERT UZ ga xush kelibsiz!\n\n"
        "Matematika Milliy Sertifikat mock testlarini ishlashingiz mumkin.",
        reply_markup=keyboard,
    )

@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "🚀 Testni boshlash — MATHCERT UZ Mini App'ni ochadi.\n"
        "📚 Qoidalar — test haqida ma'lumot.\n"
        "⭐ Premium — Premium imkoniyatlar."
    )

@dp.message(lambda message: message.text == "📚 Qoidalar")
async def rules(message: Message):
    await message.answer(
        "📚 Test tuzilishi:\n"
        "• 1–16: Y-1\n"
        "• 17–32: Y-2\n"
        "• 33–35: Moslashtirish\n"
        "• 36–45: Ochiq topshiriqlar"
    )

@dp.message(lambda message: message.text == "⭐ Premium")
async def premium(message: Message):
    await message.answer(
        "⭐ Premium: 20 000 so'm / 7 kun.\n"
        "To'lov tizimi keyingi bosqichda ulanadi."
    )

async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="MATHCERT UZ ni ochish"),
        BotCommand(command="help", description="Yordam"),
    ])

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
