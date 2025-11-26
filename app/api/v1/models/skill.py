from .. import database
from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy import Column, Integer, String, DateTime


class Skill(database.base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now(ZoneInfo("America/Sao_Paulo")))
    updated_at = Column(DateTime, default=datetime.now(ZoneInfo("America/Sao_Paulo")))
