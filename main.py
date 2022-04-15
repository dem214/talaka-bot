import asyncio
import os

from telebot.async_telebot import AsyncTeleBot


async def main():
    TOKEN = os.environ.get('TELEGRAM_TOKEN')
    if not TOKEN:
        raise ValueError('token secret is not provided')
    bot = AsyncTeleBot(TOKEN)

    @bot.message_handler(commands=['start', 'help'])
    async def send_welcome(message):
        await bot.reply_to(message, "Howdy, how are you doing?")

    await bot.infinity_polling()


if __name__ == '__main__':
    asyncio.run(main())
