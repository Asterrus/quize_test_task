from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = 'question'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    question_id: Mapped[int] = mapped_column(index=True, unique=True)
    question_text: Mapped[str]
    answer_text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    def __repr__(self) -> str:
        return f'Question(id={self.id!r}, name={self.question_text[:20]!r})'
