# app/models/schedule.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    subject = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
