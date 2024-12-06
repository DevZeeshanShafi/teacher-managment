
# app/schemas/notification.py
from pydantic import BaseModel
from datetime import datetime

class NotificationBase(BaseModel):
    message: str

class NotificationCreate(NotificationBase):
    teacher_id: int

class Notification(NotificationBase):
    id: int
    teacher_id: int
    created_at: datetime
    is_read: bool

    class Config:
        orm_mode = True