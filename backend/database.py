from prisma import Prisma
import os
import asyncio

_db_client = None

def get_db_client() -> Prisma:
    global _db_client
    if _db_client is None:
        _db_client = Prisma()
    return _db_client

async def get_db():
    db = get_db_client()
    if not db.is_connected():
        await db.connect()
    return db

async def disconnect_db():
    db = get_db_client()
    if db.is_connected():
        await db.disconnect()
