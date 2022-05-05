from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.common.jwt_decode import JwtDecoded

from src.loss_communication.schema import CreateLossCommunication, LossCommunication, UpdateLossCommunication
from src.loss_communication.service import make_loss_communication_service
from src.middlewares.jwt_required import RequiredAuth
from src.sqlalchemy.database import get_db


router = APIRouter(prefix='/loss-communication')


@router.get('', response_model=List[LossCommunication], dependencies=[Depends(RequiredAuth())])
def find_all(db: Session = Depends(get_db)):
    service = make_loss_communication_service(db)
    return service.find_all()


@router.post('', response_model=LossCommunication, dependencies=[Depends(RequiredAuth())])
def create(payload: CreateLossCommunication,
           db: Session = Depends(get_db),
           user: JwtDecoded = Depends(RequiredAuth())
           ):
    service = make_loss_communication_service(db)
    return service.create(payload, user.sub)


@router.get('/{id}', response_model=LossCommunication, dependencies=[Depends(RequiredAuth())])
def find_one(id: UUID, db: Session = Depends(get_db)):
    service = make_loss_communication_service(db)
    return service.find_one(id)


@router.delete('/{id}', dependencies=[Depends(RequiredAuth())])
def delete(id: UUID,
           db: Session = Depends(get_db),
           ) -> None:
    service = make_loss_communication_service(db)
    return service.delete(id)


@router.put('/{id}', response_model=LossCommunication, dependencies=[Depends(RequiredAuth())])
def update(id: UUID,
           payload: UpdateLossCommunication,
           db: Session = Depends(get_db)
           ):
    service = make_loss_communication_service(db)
    return service.update(id, payload)
