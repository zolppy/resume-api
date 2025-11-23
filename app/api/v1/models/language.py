from .. import database
from sqlalchemy import Column, Integer, String, DateTime


class Language(database.base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    proficiency = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
