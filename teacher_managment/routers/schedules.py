
# app/routers/schedules.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from teacher_managment import models, schemas
from typing import List

router = APIRouter(prefix="/schedules", tags=["schedules"])

@router.post("/", response_model=schemas.Schedule)
def create_schedule(schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    db_schedule = models.Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

@router.get("/teacher/{teacher_id}", response_model=List[schemas.Schedule])
def read_teacher_schedules(teacher_id: int, db: Session = Depends(get_db)):
    schedules = db.query(models.Schedule).filter(models.Schedule.teacher_id == teacher_id).all()
    return schedules
