from pydantic import PositiveInt
from typing import List, Optional
from .. import schemas, database, services
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, status, Body, Depends, Query

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
):
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
    response_model=schemas.LanguageCreate,
    summary="Create language.",
    description="Create language.",
)
async def create_language(
    db: AsyncSession = Depends(database.get_db),
    language: schemas.LanguageIn = Body(description="Language to create."),
):
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
    return await language_service.create_language(db=db, language=language)
