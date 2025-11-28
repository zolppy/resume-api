from pydantic import PositiveInt
from typing import List, Optional
from .. import schemas, database, services
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Path, status, Body, Depends, Query

language_router = APIRouter()
language_service = services.LanguageService()


@language_router.get(
    path="/",
    response_model=List[schemas.LanguageOut],
    summary="Get all languages.",
    description="Get all languages.",
)
async def get_all(
    db: AsyncSession = Depends(database.get_db),
    page: Optional[PositiveInt] = Query(ge=1, default=1, description="Page number."),
    items_per_page: Optional[PositiveInt] = Query(
        ge=1, default=100, description="Items per page."
    ),
) -> List[schemas.LanguageOut]:
    """
    Retrieves all languages from the database.

    Args:
        db (AsyncSession): A database session.
        page (Optional[PositiveInt]): Page number. Defaults to 1.
        items_per_page (Optional[PositiveInt]): Items per page. Defaults to 100.

    Returns:
        List[schemas.LanguageOut]: List of languages.
    """
    return await language_service.get_all(
        db=db, page=page, items_per_page=items_per_page
    )


@language_router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.LanguageOut,
    summary="Create language.",
    description="Create language.",
)
async def create(
    db: AsyncSession = Depends(database.get_db),
    language: schemas.LanguageIn = Body(description="Language to create."),
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
    return await language_service.create(db=db, language=language)


@language_router.delete(
    path="/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete language.",
    description="Delete language.",
)
async def delete_by_id(
    db: AsyncSession = Depends(database.get_db),
    id: PositiveInt = Path(description="Language ID to delete."),
) -> None:
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
    return await language_service.delete_by_id(db=db, id=id)


@language_router.patch(
    path="/{id}",
    response_model=schemas.LanguageOut,
    summary="Update language.",
    description="Update language.",
)
async def update_by_id(
    db: AsyncSession = Depends(database.get_db),
    id: PositiveInt = Path(description="Language ID to update."),
    language: schemas.LanguageUpdate = Body(description="Language to update."),
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
    return await language_service.update_by_id(db=db, id=id, language=language)
