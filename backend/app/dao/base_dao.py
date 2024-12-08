from sqlalchemy import select, delete, update, insert

from app.database import async_session_marker


class BaseDao:
    """Default view queries"""
    model = None

    """GET"""
    @classmethod
    async def get_all(cls, **filter_by):
        async with async_session_marker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_by_id(cls, model_id):
        async with async_session_marker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_one_or_none(cls, **filter_by):
        async with async_session_marker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    """POST"""
    @classmethod
    async def add_item(cls, **data):
        async with async_session_marker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    """DELETE"""
    @classmethod
    async def delete_by_id(cls, model_id: int):
        async with async_session_marker() as session:
            query = delete(cls.model).filter_by(id=model_id)
            await session.execute(query)
            await session.commit()

    """UPDATE"""
    @classmethod
    async def update_by_id(cls, model_id: int, **data):
        async with async_session_marker() as session:
            query = update(cls.model).filter_by(id=model_id).values(**data)
            await session.execute(query)
            await session.commit()
