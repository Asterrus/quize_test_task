from fastapi import FastAPI

from database.crud import get_last_question, bulk_create
from database.db import database
from schemas import Question
from utils.functions import bulk_preparation, get_unique_questions

app = FastAPI()


@app.post('/get_questions', response_model=Question | None)
async def add_questions(db: database, questions_num: int):
    """
    ## Добавление списка вопросов в базу данных.
    ### Записываются только уникальные вопросы.
    ### Возвращается последний записанный в базу вопрос или None если его нет.
    """
    last_question = await get_last_question(db)
    questions = await get_unique_questions(db, questions_num)
    questions = await bulk_preparation(questions)
    await bulk_create(db, questions)
    return last_question
