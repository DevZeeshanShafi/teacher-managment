
# app/schemas/performance.py
from pydantic import BaseModel

class PerformanceBase(BaseModel):
    student_satisfaction: float
    attendance_rate: float
    average_grade: float

class PerformanceCreate(PerformanceBase):
    teacher_id: int

class Performance(PerformanceBase):
    id: int
    teacher_id: int

    class Config:
        orm_mode = True
