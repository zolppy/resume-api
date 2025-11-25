from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy import select
from .. import schemas, models
from pydantic import PositiveInt
from fastapi import HTTPException, status
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
    async def create(db: AsyncSession, language: schemas.LanguageIn):
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

    @staticmethod
    async def delete_by_id(db: AsyncSession, id: PositiveInt) -> None:
        """
        Deletes a language by its ID from the database.

        Args:
            db (AsyncSession): A database session.
            id (PositiveInt): The ID of the language to delete.

        Returns:
            None

        Raises:
            HTTPException: If the language does not exist (404) or if there is an internal server error (500).
        """
        language = await db.get(models.Language, id)
        if not language:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Language not found.",
            )
        await db.delete(language)
        await db.commit()
