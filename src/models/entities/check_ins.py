from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func

class CheckIns(Base):
    __tablename__ = "checkIns"

    id = Column(String, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendee_Id = Column(String, ForeignKey("attendees.id"))

    def __repr__(self):
        return f"CheckIns [attendee_Id={self.attendee_Id}]"
