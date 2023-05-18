from datetime import datetime

import httpx
from sqlalchemy.ext.asyncio import AsyncSession

from database.crud import get_questions_ids

URL = f"https://jservice.io/api/random?count="


def date_converter(date_string):
    """Возвращает объект datetime вместо строки"""
    date_format = '%Y-%m-%dT%H:%M:%S.%fZ'
    return datetime.strptime(date_string, date_format)


async def bulk_preparation(questions):
    """Возвращает подготовленный для bulk_insert список вопросов"""
    for question in questions:
        question['question_id'] = question['id']
        question.pop('id')
        question['question_text'] = question['question']
        question['answer_text'] = question['answer']
        question['created_at'] = date_converter(question['created_at'])
    return questions


async def get_questions(amount=1) -> list[dict]:
    """Возвращает список вопросов"""
    async with httpx.AsyncClient() as client:
        response = await client.get(URL + str(amount))
        questions = response.json()
    return questions


async def get_unique_questions(db: AsyncSession, amount=1):
    """Возвращает список уникальных вопросов."""
    unique_questions = 0
    questions = []
    questions_remain = amount
    ids = set(await get_questions_ids(db))
    while unique_questions != amount:
        new_questions = await get_questions(questions_remain)
        unique_new = list(filter(lambda x: x['id'] not in ids, new_questions))
        questions += unique_new
        unique_questions = len(questions)
        questions_remain = amount - len(questions)
    return questions
