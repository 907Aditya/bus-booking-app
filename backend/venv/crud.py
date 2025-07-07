from sqlalchemy.orm import Session
import models, schemas

def create_cargo(db: Session, cargo_data: schemas.CargoCreate):
    db_cargo = models.Cargo(**cargo_data.dict())
    db.add(db_cargo)
    db.commit()
    db.refresh(db_cargo)
    return db_cargo
