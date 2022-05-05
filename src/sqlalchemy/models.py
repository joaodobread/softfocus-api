import uuid
from datetime import datetime

from geoalchemy2 import Geometry
from sqlalchemy import ForeignKey, Integer, String, DateTime, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column

from .database import Base


class Analysts(Base):
    __tablename__ = 'analysts'
    id = Column(UUID(as_uuid=True),
                primary_key=True, default=uuid.uuid4)
    name = Column(String(300), nullable=False)
    email = Column(String(300), nullable=False)
    password = Column(String(300), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    is_super = Column(Boolean, nullable=False, default=False)
    loss_communication = relationship('LossCommunication', lazy='noload')


class LossCommunication(Base):
    __tablename__ = 'loss_communication'
    id = Column(UUID(as_uuid=True),
                primary_key=True, default=uuid.uuid4)
    analysts_id = Column(Integer, ForeignKey('analysts.id'))
    analyst = relationship(
        'Analysts', back_populates='loss_communication', lazy='joined')
    farmer_name = Column(String(300), nullable=False)
    farmer_email = Column(String(300), nullable=False)
    farmer_document = Column(String(20), nullable=False)
    location = Column(Geometry(geometry_type='POINT',
                               srid=4326), nullable=False)
    harvest_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    couse_of_loss = Column(
        Enum('excessive_rain', 'frost', 'hail', 'dry', 'gale', 'ray'), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    deleted = Column(Boolean, nullable=True, default=False)
