import asyncio
import os

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from telebot.async_telebot import AsyncTeleBot

from talaka_bot.database import clear_all, get_session, engine


async def async_main():

    await clear_all()

    async with get_session()() as session:
        async with session.begin():

            TOKEN = os.environ.get('TELEGRAM_TOKEN')
            if not TOKEN:
                raise ValueError('token secret is not provided')
            bot = AsyncTeleBot(TOKEN)

            @bot.message_handler(commands=['start', 'help'])
            async def send_welcome(message)
                await bot.reply_to(message, "Howdy, how are you doing?")

            await bot.infinity_polling()



if __name__ == '__main__':
    asyncio.run(async_main())
