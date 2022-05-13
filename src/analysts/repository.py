from typing import List
from sqlalchemy.orm import Session

from src.analysts.schema import CreateAnalystsModel
from src.sqlalchemy.models import Analysts


class AnalystsRepository:
    def __init__(self,  db: Session) -> None:
        self.db = db

    def find_by_email(self, email: str) -> Analysts:
        return self.db.query(Analysts).filter_by(email=email).first()

    def find_all(self) -> List[Analysts]:
        return self.db.query(Analysts).all()

    def create(self, payload: CreateAnalystsModel) -> Analysts:
        analyst = Analysts(
            name=payload.name,
            email=payload.email,
            password=payload.password,
        )
        self.db.add(analyst)
        self.db.commit()
        self.db.refresh(analyst)
        return analyst

    def __del__(self):
        self.db.close()
        self.db.close_all()
