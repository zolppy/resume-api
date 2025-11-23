from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy import select
from .. import schemas, models
from pydantic import PositiveInt
from sqlalchemy.ext.asyncio import AsyncSession


class LanguageCrud:
    @staticmethod
    async def get_all(
        db: AsyncSession,
        page: Optional[PositiveInt] = 1,
        items_per_page: Optional[PositiveInt] = 100,
    ):
        """
        Retrieves all languages from the database.

        Args:
            db (AsyncSession): A database session.
            page (Optional[PositiveInt]): Page number. Defaults to 1.
            items_per_page (Optional[PositiveInt]): Items per page. Defaults to 100.

        Returns:
            List[models.Language]: List of languages.
        """
        page = page or 1
        items_per_page = items_per_page or 100
        offset = (page - 1) * items_per_page
        query = (
            select(models.Language)
            .order_by(models.Language.id.asc())
            .offset(offset)
            .limit(items_per_page)
        )
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def create_language(db: AsyncSession, language: schemas.LanguageIn):
        """
        Creates a language in the database.

        Args:
            db (AsyncSession): A database session.
            language (schemas.LanguageIn): The language to create.

        Returns:
            models.Language: The created language.
        """
        language_dict = language.model_dump()
        language_dict["created_at"] = datetime.now(ZoneInfo("America/Sao_Paulo"))
        language = models.Language(**language_dict)
        db.add(language)
        await db.commit()
        await db.refresh(language)
        return language
