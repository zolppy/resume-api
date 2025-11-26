from typing import Optional

from pydantic import PositiveInt
from sqlalchemy import select
from .. import models, schemas
from sqlalchemy.ext.asyncio import AsyncSession


class SkillCrud:
    @staticmethod
    async def create(db: AsyncSession, skill: schemas.SkillIn):
        """
        Creates a skill in the database.

        Args:
            db (AsyncSession): A database session.
            skill (schemas.SkillIn): The skill to create.

        Returns:
            models.Skill: The created skill.
        """
        skill_dict = skill.model_dump()
        skill = models.Skill(**skill_dict)
        db.add(skill)
        await db.commit()
        await db.refresh(skill)
        return skill

    @staticmethod
    async def get_all(
        db: AsyncSession,
        page: Optional[PositiveInt] = 1,
        items_per_page: Optional[PositiveInt] = 100,
    ):
        """
        Retrieves all skills from the database.

        Args:
            db (AsyncSession): A database session.
            page (Optional[PositiveInt]): Page number. Defaults to 1.
            items_per_page (Optional[PositiveInt]): Items per page. Defaults to 100.

        Returns:
            List[models.Skill]: List of skills.
        """
        page = page or 1
        items_per_page = items_per_page or 100
        offset = (page - 1) * items_per_page
        query = (
            select(models.Skill)
            .order_by(models.Skill.id.asc())
            .offset(offset)
            .limit(items_per_page)
        )
        result = await db.execute(query)
        return result.scalars().all()
