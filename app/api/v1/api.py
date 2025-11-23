from . import routers
from fastapi import APIRouter

api_v1_router = APIRouter()

api_v1_router.include_router(
    router=routers.language_router, prefix="/languages", tags=["Languages"]
)
