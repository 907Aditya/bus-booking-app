from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# ==================== User ====================
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ==================== Bus ====================
class BusCreate(BaseModel):
    source: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    total_seats: int

class BusOut(BusCreate):
    id: int
    available_seats: int
    class Config:
        from_attributes = True


# ==================== Booking ====================
class BookingCreate(BaseModel):
    user_id: int
    bus_id: int
    seats_booked: int

class BookingOut(BaseModel):
    id: int
    user_id: int
    bus_id: int
    seats_booked: int
    class Config:
        from_attributes = True


# ==================== Cargo ====================
class CargoCreate(BaseModel):
    bus_id: int
    activity_type: str
    start_city: str
    end_city: str
    start_branch: str
    end_branch: str

    sender_name: str
    sender_mobile: str
    sender_city: str
    sender_state: str

    receiver_name: str
    receiver_mobile: str
    receiver_city: str
    receiver_state: str

    consignment_type: str
    description: str
    pack_method: str
    units: int
    goods_value: float
    weight_actual: float
    weight_cft: float
    weight_charge: float
    rate: float
    freight: float

    pickup_cartage: float
    misc_cartage: float
    drop_cartage: float
    hamali: float
    op_hamali: float
    valuation: float
    doc_fee: float
    gst_percent: float

    payment_type: str
    method_of_payment: str
    account_number: Optional[str] = None
    reference_id: Optional[str] = None

    created_at: datetime


class CargoOut(CargoCreate):
    id: int
    class Config:
        from_attributes = True
