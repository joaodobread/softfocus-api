from sqlalchemy import desc
from sqlalchemy.orm import Session

from src.loss_communication.schema import CreateLossCommunication, FindLocationConflic, Point, UpdateLossCommunication
from src.sqlalchemy.models import LossCommunication


class LossCommunicationRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def find_all(self):
        loss_communication = self.db.query(
            LossCommunication).order_by(desc(LossCommunication.created_at)).filter_by(deleted=False).all()

        return loss_communication

    def create(self, payload: CreateLossCommunication, analyst_id: str):
        loss_communication = LossCommunication(
            analysts_id=analyst_id,
            farmer_name=payload.farmer_name,
            farmer_email=payload.farmer_email,
            farmer_document=payload.farmer_document,
            harvest_date=payload.harvest_date,
            couse_of_loss=payload.couse_of_loss,
            location=f"POINT({payload.location['lat']} {payload.location['long']})",
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
        loss_communication.location = f"POINT({payload.location['lat']} {payload.location['long']})",
        loss_communication.harvest_date = payload.harvest_date
        loss_communication.couse_of_loss = payload.couse_of_loss

        self.db.merge(loss_communication)
        self.db.commit()

        return loss_communication

    def find_location_conflic(self, payload: FindLocationConflic):
        limit_distance = 10000
        location = payload.location
        harvest_date = payload.harvest_date
        couse_of_loss = payload.couse_of_loss

        query = f"""
            select
                id as id,
                lc.farmer_name as farmer_name,
                lc.location as location,
                lc.farmer_document as farmer_document,
                lc.harvest_date as harvest_date,
                lc.couse_of_loss as couse_of_loss,
                lc.farmer_email as farmer_email,
                ST_Distance(
                    st_setsrid( st_point( {location["lat"]}, {location["long"]} ) , 4326 ),
                    st_setsrid( lc.location  , 4326 ),
                true
            ) as distance from loss_communication lc where ST_Distance(
                st_setsrid( st_point( {location["lat"]}, {location["long"]} ) , 4326 ),
                st_setsrid(  lc.location , 4326 ),
                true
            ) <= {limit_distance} and date(lc.harvest_date) = date('{harvest_date}') and lc.couse_of_loss != '{couse_of_loss}' and deleted = false

        """
        print(query)
        return self.db.execute(query).fetchall()
