from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.analysts.schema import AnalystModel, CreateAnalystsModel
from src.analysts.service import make_analyst_service
from src.middlewares.jwt_required import RequiredAuth
from src.sqlalchemy.database import get_db


router = APIRouter(prefix="/analysts")


@router.get("",  response_model=List[AnalystModel], dependencies=[Depends(RequiredAuth())])
def find_all(db: Session = Depends(get_db)):
    service = make_analyst_service(db)
    analysts = service.find_all()
    return analysts


@router.post("", response_model=AnalystModel)
def create(payload: CreateAnalystsModel, db: Session = Depends(get_db)):
    service = make_analyst_service(db)
    return service.create(payload)
