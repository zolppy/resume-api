from .. import schemas, database, services
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, status, Body, Depends

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
