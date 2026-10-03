import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    WebAppInfo,
    BotCommand,
)

# ==================================================
# TOKEN
# ==================================================

TOKEN = "BU_YERGA_BOT_TOKENINGIZNI_QO'YING"

# ==================================================
# TO'G'RI MATHCERT UZ SAYT MANZILI
# ==================================================

WEB_APP_URL = "https://raxmonjonanov77-hash.github.io/matematika-milliy-sertifikat/"

if not TOKEN:
    raise RuntimeError("BOT_TOKEN topilmadi")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ==================================================
# TELEGRAM KEYBOARD
# ==================================================

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🚀 MATHCERT TESTNI BOSHLASH",
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

# ==================================================
# START
# ==================================================

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🧮 MATHCERT UZ ga xush kelibsiz!\n\n"
        "Matematika Milliy Sertifikat mock testlarini ishlashingiz mumkin.\n\n"
        "👇 Testni boshlash uchun tugmani bosing:",
        reply_markup=keyboard,
    )

# ==================================================
# HELP
# ==================================================

@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "🚀 MATHCERT TESTNI BOSHLASH — Mini App'ni ochadi.\n"
        "📚 Qoidalar — test haqida ma'lumot.\n"
        "⭐ Premium — Premium imkoniyatlar."
    )

# ==================================================
# QOIDALAR
# ==================================================

@dp.message(lambda message: message.text == "📚 Qoidalar")
async def rules(message: Message):
    await message.answer(
        "📚 Test tuzilishi:\n\n"
        "• 1–16: Y-1\n"
        "• 17–32: Y-2\n"
        "• 33–35: Moslashtirish\n"
        "• 36–45: Ochiq topshiriqlar"
    )

# ==================================================
# PREMIUM
# ==================================================

@dp.message(lambda message: message.text == "⭐ Premium")
async def premium(message: Message):
    await message.answer(
        "⭐ Premium\n\n"
        "20 000 so'm / 7 kun.\n"
        "To'lov tizimi keyingi bosqichda ulanadi."
    )

# ==================================================
# MAIN
# ==================================================

async def main():

    await bot.set_my_commands([
        BotCommand(
            command="start",
            description="MATHCERT UZ ni ochish"
        ),
        BotCommand(
            command="help",
            description="Yordam"
        ),
    ])

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
