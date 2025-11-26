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
