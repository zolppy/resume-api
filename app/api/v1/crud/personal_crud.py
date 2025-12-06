from .. import schemas, models
from sqlalchemy.ext.asyncio import AsyncSession


class PersonalCrud:
    @staticmethod
    async def create(db: AsyncSession, personal: schemas.PersonalIn):
        personal_dict = personal.model_dump()
        personal = models.Personal(**personal_dict)
        db.add(personal)
        await db.commit()
        await db.refresh(personal)
        return personal
