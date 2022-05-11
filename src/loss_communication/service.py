from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import json
from plpygis import Geometry


from src.loss_communication.schema import CreateLossCommunication, FindLocationConflic, Point, UpdateLossCommunication
from .repository import LossCommunicationRepository


def make_loss_communication_service(db: Session):
    repository = LossCommunicationRepository(db)
    return LossCommunicationService(repository)


class LossCommunicationService:
    def __init__(self, repository: LossCommunicationRepository) -> None:
        self.repository = repository

    def binary_location_to_json(self, location):
        return json.dumps(Geometry(location).geojson)

    def find_all(self):
        loss_communication = self.repository.find_all()
        for loss in loss_communication:
            loss.location = self.binary_location_to_json(loss.location)
        return loss_communication

    def create(self, payload: CreateLossCommunication, analyst_id: str):
        loss_communication = self.repository.create(payload, analyst_id)
        loss_communication.location = self.binary_location_to_json(
            loss_communication.location)
        return loss_communication

    def find_one(self, id: str):
        loss_communication = self.repository.find_one(id)
        if not loss_communication:
            raise HTTPException(status.HTTP_404_NOT_FOUND,
                                "loss_communication_not_found")
        loss_communication.location = self.binary_location_to_json(
            loss_communication.location)
        return loss_communication

    def delete(self, id: str):
        loss_communication = self.repository.delete(id)
        if not loss_communication:
            raise HTTPException(status.HTTP_404_NOT_FOUND,
                                "loss_communication_not_found")
        return loss_communication

    def update(self, id: str, payload: UpdateLossCommunication):
        loss_communication = self.repository.update(id, payload)
        if not loss_communication:
            raise HTTPException(status.HTTP_404_NOT_FOUND,
                                "loss_communication_not_found")
        loss_communication.location = self.binary_location_to_json(
            loss_communication.location)
        return loss_communication

    def find_location_conflic(self, payload: FindLocationConflic):
        loss_communication = self.repository.find_location_conflic(payload)
        return [
            {
                "id": loss.id,
                "farmer_name": loss.farmer_name,
                "farmer_document": loss.farmer_document,
                "harvest_date": loss.harvest_date,
                "couse_of_loss": loss.couse_of_loss,
                "farmer_email": loss.farmer_email,
                "location": self.binary_location_to_json(loss.location)
            } for loss in loss_communication
        ]
