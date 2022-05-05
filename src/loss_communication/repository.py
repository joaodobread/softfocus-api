from sqlalchemy.orm import Session

from src.loss_communication.schema import CreateLossCommunication, UpdateLossCommunication
from src.sqlalchemy.models import LossCommunication


class LossCommunicationRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def find_all(self):
        loss_communication = self.db.query(
            LossCommunication).filter_by(deleted=False).all()

        return loss_communication

    def create(self, payload: CreateLossCommunication, analyst_id: str):
        loss_communication = LossCommunication(
            analysts_id=analyst_id,
            farmer_name=payload.farmer_name,
            farmer_email=payload.farmer_email,
            farmer_document=payload.farmer_document,
            harvest_date=payload.harvest_date,
            couse_of_loss=payload.couse_of_loss,
            location=f"POINT({payload.location['long']} {payload.location['lat']})",
        )
        self.db.add(loss_communication)
        self.db.commit()
        self.db.refresh(loss_communication)

        return loss_communication

    def find_one(self, id: str):
        loss_communication = self.db.query(
            LossCommunication).filter_by(id=id, deleted=False).first()
        return loss_communication

    def delete(self, id: str):
        loss_communication = self.db.query(
            LossCommunication).filter_by(id=id, deleted=False).first()
        if not loss_communication:
            return None
        loss_communication.deleted = True
        self.db.merge(loss_communication)
        self.db.commit()
        return loss_communication

    def update(self, id: str, payload: UpdateLossCommunication):
        loss_communication: LossCommunication = self.db.query(
            LossCommunication).filter_by(id=id, deleted=False).first()

        if not loss_communication:
            return None

        loss_communication.farmer_name = payload.farmer_name
        loss_communication.farmer_email = payload.farmer_email
        loss_communication.farmer_document = payload.farmer_document
        loss_communication.location = f"POINT({payload.location['long']} {payload.location['lat']})",
        loss_communication.harvest_date = payload.harvest_date
        loss_communication.couse_of_loss = payload.couse_of_loss

        self.db.merge(loss_communication)
        self.db.commit()

        return loss_communication
