from .. import database
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime


class Personal(database.base):
    __tablename__ = "personal"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    full_name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(String(50), nullable=False, unique=True)
    job_title = Column(String(50), nullable=False)
    github_link = Column(String(50), nullable=False, unique=True)
    linkedin_link = Column(String(50), nullable=False, unique=True)
    professional_summary = Column(String(500), nullable=False)

    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )
