from typing import Optional
from sqlalchemy import select
from .. import models, schemas
from pydantic import PositiveInt
from fastapi import HTTPException, status
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

    @staticmethod
    async def update_by_id(
        db: AsyncSession, id: PositiveInt, skill: schemas.SkillUpdate
    ) -> models.Skill:
        """
        Updates a skill by its ID in the database.

        Args:
            db (AsyncSession): A database session.
            id (PositiveInt): The ID of the skill to update.
            skill (schemas.SkillUpdate): The skill update data.

        Returns:
            models.Skill: The updated skill.

        Raises:
            HTTPException: If the skill does not exist (404).
        """
        update_data = skill.model_dump(exclude_unset=True)
        skill = await db.get(models.Skill, id)
        if not skill:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Language not found."
            )
        for field, value in update_data.items():
            setattr(skill, field, value)
        await db.commit()
        await db.refresh(skill)
        return skill
