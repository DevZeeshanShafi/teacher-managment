
# app/models/performance.py
from sqlalchemy import Column, Integer, Float, ForeignKey
from database import Base

class Performance(Base):
    __tablename__ = "performances"

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    student_satisfaction = Column(Float)
    attendance_rate = Column(Float)
    average_grade = Column(Float)
