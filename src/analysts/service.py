from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.analysts.repository import AnalystsRepository
from src.analysts.schema import CreateAnalystsModel
from src.common.bcrypt import BcryptAdapter
from src.sqlalchemy.models import Analysts


def make_analyst_service(db: Session):
    return AnalystsService(AnalystsRepository(db), BcryptAdapter())


class AnalystsService:
    def __init__(self, repository: AnalystsRepository, bcrypt: BcryptAdapter) -> None:
        self.repository = repository
        self.bcrypt = bcrypt

    def find_by_email(self, email: str) -> Analysts:
        analyst = self.repository.find_by_email(email)
        if not analyst:
            raise HTTPException(status.HTTP_404_NOT_FOUND, 'analyst_not_found')
        return analyst

    def find_all(self) -> List[Analysts]:
        return self.repository.find_all()

    def create(self, payload: CreateAnalystsModel):
        if self.repository.find_by_email(payload.email):
            raise HTTPException(status.HTTP_409_CONFLICT,
                                'email_already_exists')
        payload.password = self.bcrypt.hash_password(payload.password)
        return self.repository.create(payload)
