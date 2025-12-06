from .. import schemas, crud
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession


class PersonalService:
    @staticmethod
    async def create(
        db: AsyncSession, personal: schemas.PersonalIn
    ) -> schemas.PersonalOut:
        try:
            created_personal = await crud.PersonalCrud.create(db=db, personal=personal)
            return schemas.PersonalOut.model_validate(created_personal)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Personal already exists.",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to create personal: {str(e)}",
            )
