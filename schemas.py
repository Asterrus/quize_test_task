from datetime import datetime

from pydantic import BaseModel


class QuestionBase(BaseModel):
    question_id: int
    question_text: str
    answer_text: str
    created_at: datetime


class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True
