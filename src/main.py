import asyncio
from os import getenv

from aiogram import (
    Bot,
    Dispatcher,
)
from aiogram.filters import Command
from aiogram.types import Message


# TOKEN = getenv("TOKEN")
TOKEN = "8427218571:AAHRcssakWWetUxum8F6_vMziGrF-ntTtrA"

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет! Я бот, сделанный на aiogram.")


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
