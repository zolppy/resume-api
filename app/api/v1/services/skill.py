from typing import List, Optional

from pydantic import PositiveInt
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

    @staticmethod
    async def get_all(
        db: AsyncSession,
        page: Optional[PositiveInt] = 1,
        items_per_page: Optional[PositiveInt] = 100,
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
        try:
            skills = await skill_crud.get_all(
                db=db, page=page, items_per_page=items_per_page
            )
            if not skills:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Skills not found."
                )
            return [schemas.SkillOut.model_validate(s) for s in skills]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to get skills: {str(e)}",
            )
