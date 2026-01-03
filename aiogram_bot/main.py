import asyncio
import httpx
from aiogram import Bot, Dispatcher, F
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters import Command
from aiogram.types import Message
from config import API_token, proxy_port, API_URL

async def main():
    session = AiohttpSession(proxy=proxy_port)
    bot = Bot(token=API_token, session=session)
    
    dp = Dispatcher()
    
    async def get_api_reply(user_id: int, username: str, user_message: str) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                API_URL, 
                json={
                    "user_id": user_id,
                    "username": username,
                    "message": user_message,
                },
                timeout=10,
            )
            return response.json().get("reply", "پاسخی دریافت نشد")


    @dp.message(Command("start"))
    async def start_command(message: Message):
        await message.answer("سلام! خوش آمدی 😊 این ربات آماده پاسخگویی است.")

    @dp.message(F.text)
    async def handle_message(message: Message):
        reply = await get_api_reply(
            message.from_user.id,
            message.from_user.username,
            message.text
        )
        await message.answer(reply)
        
        
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())