import asyncio
from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, async_session, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base


async def main():
    bot = Bot(token="8124603104:AAE_HcQptY5cUoQaq5QEP56fe0uC_Zf46WU")
    dp = Dispatcher()
    dp.include_routers(
    )

if __name__ == "__main__":
    asyncio.run(main())


