from .. import database
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime


class Language(database.base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    proficiency = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )
