from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from datetime import datetime
import uuid

router = APIRouter()

# ---------- POST: Add a Cargo Booking ----------
@router.post("/add", response_model=schemas.CargoOut)
def create_cargo(cargo: schemas.CargoCreate, db: Session = Depends(get_db)):
    # Check bus exists
    bus = db.query(models.Bus).filter(models.Bus.id == cargo.bus_id).first()
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")

    # Assign unique cargo ID (UUID or batch code)
    cargo_data = cargo.dict()
    cargo_data["created_at"] = datetime.now()

    new_cargo = models.Cargo(**cargo_data)
    db.add(new_cargo)
    db.commit()
    db.refresh(new_cargo)
    return new_cargo

# ---------- GET: List All Cargo Bookings ----------
@router.get("/all", response_model=list[schemas.CargoOut])
def list_all_cargo(db: Session = Depends(get_db)):
    return db.query(models.Cargo).order_by(models.Cargo.created_at.desc()).all()

# ---------- GET: Get Cargo By Bus ID ----------
@router.get("/bus/{bus_id}", response_model=list[schemas.CargoOut])
def get_cargo_by_bus(bus_id: int, db: Session = Depends(get_db)):
    return db.query(models.Cargo).filter(models.Cargo.bus_id == bus_id).order_by(models.Cargo.created_at.desc()).all()

# ---------- GET: Single Cargo by ID ----------
@router.get("/{cargo_id}", response_model=schemas.CargoOut)
def get_cargo_by_id(cargo_id: int, db: Session = Depends(get_db)):
    cargo = db.query(models.Cargo).filter(models.Cargo.id == cargo_id).first()
    if not cargo:
        raise HTTPException(status_code=404, detail="Cargo not found")
    return cargo

# ---------- Test Route ----------
@router.get("/test")
def test_cargo():
    return {"message": "✅ Cargo router working!"}
