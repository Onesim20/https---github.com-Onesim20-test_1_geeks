import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from database import db
from config import BOT_TOKEN
from handlers.common import COMMANDS
from handlers.common import router as common_router
from handlers.fsm import router as fsm_router


async def set_bot_commands(bot: Bot) -> None:
    await bot.set_my_commands(
        [BotCommand(command=cmd, description=desc) for cmd, desc in COMMANDS]
    )


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    db.init_db()

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    
    dp.include_router(fsm_router)
    dp.include_router(common_router)

    await set_bot_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
