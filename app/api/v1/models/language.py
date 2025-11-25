from .. import database
from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy import Column, Integer, String, DateTime


class Language(database.base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    proficiency = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(ZoneInfo("America/Sao_Paulo")))
