
from pydantic import BaseModel


class LossCommunication(BaseModel):
    id: int
    farmer_name: str
    farmer_document: str
    farmer_email: str

    class Config:
        orm_mode = True
