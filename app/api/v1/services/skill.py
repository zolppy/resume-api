from .. import schemas, crud
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

skill_crud = crud.SkillCrud()


class SkillService:
    @staticmethod
    async def create(db: AsyncSession, skill: schemas.SkillIn) -> schemas.SkillOut:
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
        try:
            created_skill = await skill_crud.create(db=db, skill=skill)
            return schemas.SkillOut.model_validate(created_skill)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Skill already exists.",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to create skill: {str(e)}",
            )
