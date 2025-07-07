from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter()

@router.post("/book", response_model=schemas.BookingOut)
def book_ticket(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    bus = db.query(models.Bus).filter(models.Bus.id == booking.bus_id).first()
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    if bus.available_seats < booking.seats_booked:
        raise HTTPException(status_code=400, detail="Not enough seats available")

    bus.available_seats -= booking.seats_booked
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@router.get("/test")
def test():
    return {"message": "Bookings router working!"}
