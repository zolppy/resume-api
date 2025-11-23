from pydantic import BaseModel, Field, AnyHttpUrl


class RootOut(BaseModel):
    docs_url: AnyHttpUrl = Field(
        description="The URL for the Swagger UI documentation.",
        examples=["http://127.0.0.1:8000/docs"],
    )
    redoc_url: AnyHttpUrl = Field(
        description="The URL for the ReDoc documentation.",
        examples=["http://127.0.0.1:8000/redoc"],
    )
