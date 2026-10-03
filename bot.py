import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    WebAppInfo,
    BotCommand,
)

# ==================================================
# SOZLAMALAR
# ==================================================

TOKEN = os.getenv("BOT_TOKEN")

# GitHub Pages manzilingiz
WEB_APP_URL = "https://raxmonjonov77-hash.github.io/matematika-milliy-sertifikat/"

if not TOKEN:
    raise RuntimeError("BOT_TOKEN Railway Variables ichida topilmadi")

# ==================================================
# BOT
# ==================================================

bot = Bot(token=TOKEN)
dp = Dispatcher()


# ==================================================
# KEYBOARD
# ==================================================

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🚀 MATHCERT TESTNI BOSHLASH",
                web_app=WebAppInfo(url=WEB_APP_URL),
            )
        ],
        [
            KeyboardButton(text="📚 Qoidalar"),
            KeyboardButton(text="⭐ Premium"),
        ],
    ],
    resize_keyboard=True,
)


# ==================================================
# /START
# ==================================================

@dp.message(CommandStart())
async def start(message: Message):

    # Eski keyboardni olib tashlaymiz
    await message.answer(
        "🔄 Yangi menyu yuklanmoqda...",
        reply_markup=ReplyKeyboardRemove(),
    )

    # Yangi keyboard
    await message.answer(
        "🧮 MATHCERT UZ ga xush kelibsiz!\n\n"
        "Matematika Milliy Sertifikat uchun mock testlarni "
        "ishlashingiz mumkin.\n\n"
        "🚀 Testni boshlash tugmasini bosing.",
        reply_markup=keyboard,
    )


# ==================================================
# /HELP
# ==================================================

@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "🚀 MATHCERT TESTNI BOSHLASH — Mini App'ni ochadi.\n"
        "📚 Qoidalar — test tuzilishi haqida.\n"
        "⭐ Premium — Premium imkoniyatlar haqida."
    )


# ==================================================
# QOIDALAR
# ==================================================

@dp.message(lambda message: message.text == "📚 Qoidalar")
async def rules(message: Message):
    await message.answer(
        "📚 MATHCERT UZ TEST TUZILISHI\n\n"
        "• 1–16 — Y-1\n"
        "• 17–32 — Y-2\n"
        "• 33–35 — Moslashtirish\n"
        "• 36–45 — Ochiq topshiriqlar\n\n"
        "Jami: 45 ta savol."
    )


# ==================================================
# PREMIUM
# ==================================================

@dp.message(lambda message: message.text == "⭐ Premium")
async def premium(message: Message):
    await message.answer(
        "⭐ PREMIUM\n\n"
        "💰 Narxi: 20 000 so'm\n"
        "⏳ Muddat: 7 kun\n\n"
        "Premium mocklar keyingi bosqichda ulanadi."
    )


# ==================================================
# BOTNI ISHGA TUSHIRISH
# ==================================================

async def main():

    await bot.set_my_commands(
        [
            BotCommand(
                command="start",
                description="MATHCERT UZ ni ochish",
            ),
            BotCommand(
                command="help",
                description="Yordam",
            ),
        ]
    )

    print("====================================")
    print("MATHCERT UZ BOT ISHLAMOQDA")
    print("WEB APP:")
    print(WEB_APP_URL)
    print("====================================")

    await dp.start_polling(bot)


# ==================================================
# RUN
# ==================================================

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
