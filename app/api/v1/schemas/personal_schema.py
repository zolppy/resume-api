from datetime import datetime
from typing import Union
from pydantic import BaseModel, EmailStr, Field, AnyHttpUrl, PositiveInt


class PersonalIn(BaseModel):
    full_name: str = Field(
        max_length=50,
        description="Full name of the person.",
        examples=["John Doe"],
    )
    email: EmailStr = Field(
        max_length=50,
        description="Email address of the person.",
        examples=["example@example.com"],
    )
    phone: str = Field(
        max_length=50,
        description="Phone number of the person.",
        examples=["+00 (00) 00000-0000"],
    )
    job_title: str = Field(
        max_length=50,
        description="Job title of the person.",
        examples=["Software Engineer"],
    )
    github_link: Union[AnyHttpUrl, str] = Field(
        max_length=50,
        description="GitHub link of the person.",
        examples=["https://github.com/username"],
    )
    linkedin_link: Union[AnyHttpUrl, str] = Field(
        max_length=50,
        description="LinkedIn link of the person.",
        examples=["https://linkedin.com/in/username"],
    )
    professional_summary: str = Field(
        max_length=500,
        description="Professional summary of the person.",
        examples=["I am a software engineer with 5 years of experience."],
    )


class PersonalOut(BaseModel):
    id: PositiveInt = Field(
        ge=1, description="ID of language.", examples=[1, 2, 3, 4, 5, 6]
    )
    full_name: str = Field(
        max_length=50,
        description="Full name of the person.",
        examples=["John Doe"],
    )
    email: EmailStr = Field(
        max_length=50,
        description="Email address of the person.",
        examples=["example@example.com"],
    )
    phone: str = Field(
        max_length=50,
        description="Phone number of the person.",
        examples=["+00 (00) 00000-0000"],
    )
    job_title: str = Field(
        max_length=50,
        description="Job title of the person.",
        examples=["Software Engineer"],
    )
    github_link: Union[AnyHttpUrl, str] = Field(
        max_length=50,
        description="GitHub link of the person.",
        examples=["https://github.com/username"],
    )
    linkedin_link: Union[AnyHttpUrl, str] = Field(
        max_length=50,
        description="LinkedIn link of the person.",
        examples=["https://linkedin.com/in/username"],
    )
    professional_summary: str = Field(
        max_length=500,
        description="Professional summary of the person.",
        examples=["I am a software engineer with 5 years of experience."],
    )
    created_at: datetime = Field(
        description="Date and time of language creation.",
        examples=["2023-01-01 00:00:00", "2023-02-01 00:00:00", "2023-03-01 00:00:00"],
    )
    updated_at: datetime = Field(
        description="Date and time of language update.",
        examples=["2023-01-01 00:00:00", "2023-02-01 00:00:00", "2023-03-01 00:00:00"],
    )

    class Config:
        from_attributes = True
