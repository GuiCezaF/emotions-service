from sqlalchemy import Column, Integer, Enum
from app.db.database import Base
import enum

class ModalityEnum(enum.Enum):
    audio = "audio"
    video = "video"
    text = "text"

class Emotions(Base):
    __tablename__ = "emotions"

    id = Column(Integer, primary_key=True, index=True)
    modality = Column(Enum(ModalityEnum), nullable=False)
