from typing import Optional
from datetime import datetime
from pydantic import BaseModel, PositiveInt, Field


class SkillIn(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=50,
        description="Name of skill.",
        examples=["Python", "Java", "JavaScript", "C++", "C#"],
    )


class SkillOut(SkillIn):
    id: PositiveInt = Field(
        ge=1, description="ID of skill.", examples=[1, 2, 3, 4, 5, 6]
    )
    created_at: datetime = Field(
        description="Date and time of skill creation.",
        examples=["2023-01-01 00:00:00", "2023-02-01 00:00:00", "2023-03-01 00:00:00"],
    )
    updated_at: datetime = Field(
        description="Date and time of skill update.",
        examples=["2023-01-01 00:00:00", "2023-02-01 00:00:00", "2023-03-01 00:00:00"],
    )

    class Config:
        from_attributes = True


class SkillUpdate(BaseModel):
    name: Optional[str] = Field(
        min_length=1,
        max_length=50,
        description="Name of skill.",
        examples=["Python", "Java", "JavaScript", "C++", "C#"],
    )
