import asyncio
from aiogram import Bot, Dispatcher
from handlers import main_handle
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

async def main():
    bot = Bot(token="7731624515:AAEkknexp4KrVvp-4CpLkPoVKwUU6CDDMv4")
    dp = Dispatcher()
    dp.include_routers(

    )
    DATABASE_URL = "sqlite+aiosqlite:///users.db"
    engine  = create_async_engine(DATABASE_URL)

    #async_session_factory = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

    with engine.begin() as connection:
        await connection.run_async(Base.metadata.create_all)


    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())