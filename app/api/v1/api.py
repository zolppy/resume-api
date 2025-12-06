from . import routers
from fastapi import APIRouter

api_v1_router = APIRouter()

api_v1_router.include_router(
    router=routers.language_router, prefix="/languages", tags=["Languages"]
)
api_v1_router.include_router(
    router=routers.skill_router, prefix="/skills", tags=["Skills"]
)
api_v1_router.include_router(
    router=routers.personal_router, prefix="/personal", tags=["Personal"]
)
