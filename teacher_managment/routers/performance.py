
# app/routers/performance.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from teacher_managment import models, schemas

router = APIRouter(prefix="/performance", tags=["performance"])

@router.post("/", response_model=schemas.Performance)
def create_performance(performance: schemas.PerformanceCreate, db: Session = Depends(get_db)):
    db_performance = models.Performance(**performance.dict())
    db.add(db_performance)
    db.commit()
    db.refresh(db_performance)
    return db_performance

@router.get("/teacher/{teacher_id}", response_model=schemas.Performance)
def read_teacher_performance(teacher_id: int, db: Session = Depends(get_db)):
    performance = db.query(models.Performance).filter(models.Performance.teacher_id == teacher_id).first()
    if performance is None:
        raise HTTPException(status_code=404, detail="Performance data not found")
    return performance
