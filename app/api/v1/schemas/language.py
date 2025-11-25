from .. import utils
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, PositiveInt


name_examples = ["English", "French", "Portuguese", "Italian", "Spanish", "Russian"]
proficiency_examples = [p for p in utils.Proficiency]


class LanguageUpdate(BaseModel):
    name: Optional[str] = Field(
        default=None,
        description="Name of language.",
        examples=name_examples,
    )
    proficiency: Optional[utils.Proficiency] = Field(
        default=None,
        description="Proficiency of language.",
        examples=proficiency_examples,
    )


class LanguageIn(BaseModel):
    name: str = Field(
        description="Name of language.",
        examples=name_examples,
    )
    proficiency: utils.Proficiency = Field(
        description="Proficiency of language.",
        examples=proficiency_examples,
    )


class LanguageOut(LanguageIn):
    id: PositiveInt = Field(
        ge=1, description="ID of language.", examples=[1, 2, 3, 4, 5, 6]
    )
    created_at: datetime = Field(
        description="Date and time of language creation.",
        examples=["2023-01-01 00:00:00", "2023-02-01 00:00:00", "2023-03-01 00:00:00"],
    )

    class Config:
        from_attributes = True
