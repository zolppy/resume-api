from pydantic import PositiveInt
from typing import List, Optional
from .. import schemas, database, services
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Path, Query, status, Body, Depends

skill_router = APIRouter()
skill_service = services.SkillService


@skill_router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.SkillOut,
    summary="Create skill.",
    description="Create skill.",
)
async def create(
    db: AsyncSession = Depends(database.get_db),
    skill: schemas.SkillIn = Body(description="Skill to create."),
) -> schemas.SkillOut:
    """
    Creates a skill in the database.

    Args:
        db (AsyncSession): A database session.
        skill (schemas.SkillIn): The skill to create.

    Returns:
        schemas.SkillOut: The created skill.

    Raises:
        HTTPException: If the skill already exists (409) or if there is an internal server error (500).
    """
    return await skill_service.create(db=db, skill=skill)


@skill_router.get(
    path="/",
    response_model=List[schemas.SkillOut],
    summary="Get all skills.",
    description="Get all skills.",
)
async def get_all(
    db: AsyncSession = Depends(database.get_db),
    page: Optional[PositiveInt] = Query(ge=1, default=1, description="Page number."),
    items_per_page: Optional[PositiveInt] = Query(
        ge=1, default=100, description="Items per page."
    ),
) -> List[schemas.SkillOut]:
    """
    Retrieves all skills from the database.

    Args:
        db (AsyncSession): A database session.
        page (Optional[PositiveInt]): Page number. Defaults to 1.
        items_per_page (Optional[PositiveInt]): Items per page. Defaults to 100.

    Returns:
        List[schemas.SkillOut]: List of skills.

    Raises:
        HTTPException: If skills not found (404) or if there is an internal server error (500).
    """
    return await skill_service.get_all(db=db, page=page, items_per_page=items_per_page)


@skill_router.patch(
    path="/{id}",
    response_model=schemas.SkillOut,
    summary="Update skill.",
    description="Update skill.",
)
async def update_by_id(
    db: AsyncSession = Depends(database.get_db),
    id: int = Path(gt=0, description="ID of skill."),
    skill: schemas.SkillUpdate = Body(description="Skill to update."),
) -> schemas.SkillOut:
    """
    Updates a skill in the database.

    Args:
        db (AsyncSession): A database session.
        id (int): The id of the skill to update.
        skill (schemas.SkillUpdate): The skill to update.

    Returns:
        schemas.SkillOut: The updated skill.

    Raises:
        HTTPException: If the skill does not exist (404) or if there is an internal server error (500).
    """
    return await skill_service.update_by_id(db=db, id=id, skill=skill)
