
from datetime import datetime
from enum import Enum
from typing import TypedDict
from uuid import UUID
from geojson_pydantic import Feature
from pydantic import BaseModel, EmailStr, Json, constr

from src.analysts.schema import AnalystModel


class Point(TypedDict):
    long: float
    lat: float


class CouseOfLoss(str, Enum):
    EXCESSIVE_RAIN = 'excessive_rain'
    FROST = 'frost',
    HAIL = 'hail'
    DRY = 'dry'
    GALE = 'gale'
    RAY = 'ray'


class LossCommunication(BaseModel):
    id: UUID
    analysts_id: UUID
    farmer_name: str
    farmer_email: str
    farmer_document: str
    harvest_date: datetime
    couse_of_loss: CouseOfLoss
    created_at: datetime
    deleted: bool
    location: Json
    analyst: AnalystModel

    class Config:
        orm_mode = True
        fields = {"eggs": "_eggs"}


class CreateLossCommunication(BaseModel):
    farmer_name: str
    farmer_email: EmailStr
    farmer_document: constr(regex=r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$')
    location: Point
    harvest_date: datetime
    couse_of_loss: CouseOfLoss


class UpdateLossCommunication(BaseModel):
    farmer_name: str
    farmer_email: EmailStr
    farmer_document: constr(regex=r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$')
    location: Point
    harvest_date: datetime
    couse_of_loss: CouseOfLoss
