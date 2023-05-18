from sqlalchemy import select, desc, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Question as QuestionModel


async def bulk_create(db, questions):
    """Записывает в базу данных несколько элементов одновременно"""
    try:
        await db.execute(insert(QuestionModel), questions)
        await db.commit()
    except Exception as e:
        db.rollback()
        print(e)


async def get_last_question(db: AsyncSession):
    """Получает последний записанный в базу вопрос"""
    query = select(QuestionModel).order_by(desc(QuestionModel.id))
    result = await db.execute(query)
    return result.scalar()


async def get_questions_ids(db: AsyncSession):
    """Получает список id вопросов"""
    query = select(QuestionModel.question_id)
    result = await db.execute(query)
    return result.scalars().all()
