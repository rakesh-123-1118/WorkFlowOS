from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

mongo_client = AsyncIOMotorClient(settings.mongo_uri)
mongo_db = mongo_client[settings.mongo_db_name]


async def ping_db() -> bool:
    try:
        await mongo_db.command("ping")
        return True
    except Exception:
        return False
