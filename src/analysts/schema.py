
from typing import List
from uuid import UUID
from pydantic import BaseModel, EmailStr, constr


class CreateAnalystsModel(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    name: str


class CreateAnalystsModelDTO(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    fullName: str


class AnalystModel(BaseModel):
    id: UUID
    email: str
    name: str

    class Config:
        orm_mode = True
