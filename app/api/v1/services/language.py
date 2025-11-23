from typing import Optional
from .. import schemas, crud
from pydantic import PositiveInt
from fastapi import status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

language_crud = crud.LanguageCrud()


class LanguageService:
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
            List[schemas.LanguageOut]: List of languages.

        Raises:
            HTTPException: If languages not found (404) or if there is an internal server error (500).
        """
        try:
            languages = await language_crud.get_all(
                db=db, page=page, items_per_page=items_per_page
            )
            if not languages:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Languages not found."
                )
            return [
                schemas.LanguageOut.model_validate(language) for language in languages
            ]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to get languages: {str(e)}",
            )

    @staticmethod
    async def create_language(db: AsyncSession, language: schemas.LanguageIn):
        """
        Creates a language in the database.

        Args:
            db (AsyncSession): A database session.
            language (schemas.LanguageIn): The language to create.

        Returns:
            schemas.LanguageCreate: The created language.

        Raises:
            HTTPException: If the language already exists (409) or if there is an internal server error (500).
        """
        try:
            created_language = await language_crud.create_language(
                db=db, language=language
            )
            return schemas.LanguageCreate.model_validate(created_language)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to create language: {str(e)}",
            )
