
# app/models/notification.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    message = Column(String)
    created_at = Column(DateTime)
    is_read = Column(Boolean, default=False)