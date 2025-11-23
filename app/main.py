from pydantic import AnyHttpUrl
from fastapi import FastAPI, Request
from .api.v1 import schemas, database, api_v1_router


app = FastAPI(
    title="The Resume API",
    description="""
    Manages Resume's data.
    """,
    version="0.03.0",
)


# TODO: migrate this to lifespan later
@app.on_event("startup")
async def startup_event():
    await database.create_tables()


app.include_router(router=api_v1_router, prefix="/api/v1")


@app.get(
    path="/",
    response_model=schemas.RootOut,
    summary="Get the URLs for the API documentation.",
)
def root(request: Request):
    """
    This endpoint returns the URLs for the API documentation.

    Args:
        request (Request): The incoming request.

    Returns:
        schemas.RootOut: A Pydantic model containing the URLs for the API documentation.
    """
    base_url = str(request.base_url)
    docs_url = base_url.rstrip("/") + str(app.docs_url)
    redoc_url = base_url.rstrip("/") + str(app.redoc_url)
    return schemas.RootOut(
        docs_url=AnyHttpUrl(docs_url), redoc_url=AnyHttpUrl(redoc_url)
    )
