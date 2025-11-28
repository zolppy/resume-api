from .. import schemas, crud
from pydantic import PositiveInt
from typing import List, Optional
from fastapi import status, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


class LanguageService:
    @staticmethod
    async def get_all(
        db: AsyncSession,
        page: Optional[PositiveInt] = 1,
        items_per_page: Optional[PositiveInt] = 100,
    ) -> List[schemas.LanguageOut]:
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
            languages = await crud.LanguageCrud.get_all(
                db=db, page=page, items_per_page=items_per_page
            )
            if not languages:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Languages not found."
                )
            return [schemas.LanguageOut.model_validate(l) for l in languages]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to get languages: {str(e)}",
            )

    @staticmethod
    async def create(
        db: AsyncSession, language: schemas.LanguageIn
    ) -> schemas.LanguageOut:
        """
        Creates a language in the database.

        Args:
            db (AsyncSession): A database session.
            language (schemas.LanguageIn): The language to create.

        Returns:
            schemas.LanguageOut: The created language.

        Raises:
            HTTPException: If the language already exists (409) or if there is an internal server error (500).
        """
        try:
            created_language = await crud.LanguageCrud.create(db=db, language=language)
            return schemas.LanguageOut.model_validate(created_language)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Language already exists.",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to create language: {str(e)}",
            )

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
        try:
            await crud.LanguageCrud.delete_by_id(db=db, id=id)
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to delete language: {str(e)}",
            )

    @staticmethod
    async def update_by_id(
        db: AsyncSession, id: PositiveInt, language: schemas.LanguageUpdate
    ) -> schemas.LanguageOut:
        """
        Updates a language by its ID in the database.

        Args:
            db (AsyncSession): A database session.
            id (PositiveInt): The ID of the language to update.
            language (schemas.LanguageUpdate): The language to update.

        Returns:
            schemas.LanguageOut: The updated language.

        Raises:
            HTTPException: If the language does not exist (404) or if there is an internal server error (500).
        """
        try:
            updated_language = await crud.LanguageCrud.update_by_id(
                db=db, id=id, language=language
            )
            return schemas.LanguageOut.model_validate(updated_language)
        except HTTPException:
            raise
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Language with this name already exists.",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to update language: {str(e)}",
            )
