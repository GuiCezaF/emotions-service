import uuid
import enum
from sqlalchemy import Column, ForeignKey, String, Float, DateTime, Enum, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base


class ModalityEnum(enum.Enum):
    audio = "audio"
    video = "video"
    text = "text"


class Emotion(Base):
    __tablename__ = "emotions"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, unique=True, nullable=False)
    modality = Column(
        Enum(ModalityEnum, name="modality"),
        nullable=False
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey(
        "users.id"), nullable=False)
    user = relationship("User", backref="emotions")
    emotion = Column(String(20), nullable=False)   # ex: happy, sad
    confidence = Column(Float, nullable=False)     # ex: 0.95
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
