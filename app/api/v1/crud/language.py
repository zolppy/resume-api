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
    async def delete_by_id(db: AsyncSession, id: PositiveInt):
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

    @staticmethod
    async def update_by_id(
        db: AsyncSession, id: PositiveInt, language_update: schemas.LanguageUpdate
    ) -> models.Language:
        """
        Updates a language by its ID in the database.

        Args:
            db (AsyncSession): A database session.
            id (PositiveInt): The ID of the language to update.
            language_update (schemas.LanguageUpdate): The language update data.

        Returns:
            models.Language: The updated language.

        Raises:
            HTTPException: If the language does not exist (404).
        """
        language = await db.get(models.Language, id)
        if not language:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Language not found.",
            )
        update_data = language_update.model_dump(exclude_unset=True)
        if update_data:
            current_time = datetime.now(ZoneInfo("America/Sao_Paulo"))
            update_data["updated_at"] = current_time
        for field, value in update_data.items():
            setattr(language, field, value)
        await db.commit()
        await db.refresh(language)
        return language
