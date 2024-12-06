
# app/routers/notifications.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from teacher_managment  import models, schemas
from typing import List
from datetime import datetime

router = APIRouter(prefix="/notifications", tags=["notifications"])

@router.post("/", response_model=schemas.Notification)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):
    db_notification = models.Notification(**notification.dict(), created_at=datetime.utcnow())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

@router.get("/teacher/{teacher_id}", response_model=List[schemas.Notification])
def read_teacher_notifications(teacher_id: int, db: Session = Depends(get_db)):
    notifications = db.query(models.Notification).filter(models.Notification.teacher_id == teacher_id).all()
    return notifications

@router.put("/{notification_id}/read", response_model=schemas.Notification)
def mark_notification_as_read(notification_id: int, db: Session = Depends(get_db)):
    notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    notification.is_read = True
    db.commit()
    db.refresh(notification)
    return notification