from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from datetime import datetime

router = APIRouter()

@router.post("/add", response_model=schemas.BusOut)
def add_bus(bus: schemas.BusCreate, db: Session = Depends(get_db)):
    new_bus = models.Bus(**bus.dict(), available_seats=bus.total_seats)
    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)
    return new_bus

@router.get("/test")
def test():
    return {"message": "Buses router working!"}
