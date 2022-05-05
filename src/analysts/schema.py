
from typing import List
from uuid import UUID
from pydantic import BaseModel

from src.schema import LossCommunication


class CreateAnalystsModel(BaseModel):
    email: str
    password: str
    name: str


class AnalystModel(BaseModel):
    id: UUID
    is_super: bool
    email: str
    name: str
    loss_communication: List[LossCommunication] = []

    class Config:
        orm_mode = True
