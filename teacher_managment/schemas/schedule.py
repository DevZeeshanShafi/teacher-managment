
# app/schemas/schedule.py
from pydantic import BaseModel
from datetime import datetime

class ScheduleBase(BaseModel):
    subject: str
    start_time: datetime
    end_time: datetime

class ScheduleCreate(ScheduleBase):
    teacher_id: int

class Schedule(ScheduleBase):
    id: int
    teacher_id: int

    class Config:
        orm_mode = True
