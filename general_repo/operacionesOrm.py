from sqlalchemy.ext.asyncio import AsyncSession


class OperacionesOrm:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add(self, obj):
        self.db.add(obj)

    async def flush(self):
        await self.db.flush()

    async def refresh(self, obj):
        await self.db.refresh(obj)

    async def add_and_refresh(self, obj):
        self.db.add(obj)
        await self.db.flush()
        await self.db.refresh(obj)
        return obj
