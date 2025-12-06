from .. import schemas, database, services
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Body, Depends, status

personal_router = APIRouter()


@personal_router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.PersonalOut,
    summary="Create contact.",
    description="Create contact.",
)
async def create(
    db: AsyncSession = Depends(database.get_db),
    personal: schemas.PersonalIn = Body(description="Contact to create."),
) -> schemas.PersonalOut:
    return await services.PersonalService.create(db=db, personal=personal)
