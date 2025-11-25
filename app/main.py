from pydantic import AnyHttpUrl
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from .api.v1 import schemas, database, api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.create_tables()
    yield


app = FastAPI(
    title="The Resume API",
    description="""
    Manages Resume's data.
    """,
    version="0.04.1",
    lifespan=lifespan,
)

app.include_router(router=api_v1_router, prefix="/api/v1")


@app.get(
    path="/",
    response_model=schemas.RootOut,
    summary="Get the URLs for the API documentation.",
    description="Get the URLs for the API documentation.",
)
def root(request: Request) -> schemas.RootOut:
    base_url = str(request.base_url)
    docs_url = base_url.rstrip("/") + str(app.docs_url)
    redoc_url = base_url.rstrip("/") + str(app.redoc_url)
    return schemas.RootOut(
        docs_url=AnyHttpUrl(docs_url), redoc_url=AnyHttpUrl(redoc_url)
    )
