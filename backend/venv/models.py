
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    bookings = relationship("Booking", back_populates="user")

class Bus(Base):
    __tablename__ = "buses"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String)
    destination = Column(String)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    total_seats = Column(Integer)
    available_seats = Column(Integer)
    bookings = relationship("Booking", back_populates="bus")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    bus_id = Column(Integer, ForeignKey("buses.id"))
    seats_booked = Column(Integer)

    user = relationship("User", back_populates="bookings")
    bus = relationship("Bus", back_populates="bookings")

class Cargo(Base):
    __tablename__ = "cargo"
    id = Column(Integer, primary_key=True, index=True)
    
    bus_id = Column(Integer, ForeignKey("buses.id"))  # Associate cargo with a bus
    
    activity_type = Column(String)  # Booking, Dispatch, etc.
    start_city = Column(String)
    end_city = Column(String)
    start_branch = Column(String)
    end_branch = Column(String)

    sender_name = Column(String)
    sender_mobile = Column(String)
    sender_city = Column(String)
    sender_state = Column(String)

    receiver_name = Column(String)
    receiver_mobile = Column(String)
    receiver_city = Column(String)
    receiver_state = Column(String)

    consignment_type = Column(String)
    description = Column(String)
    pack_method = Column(String)
    units = Column(Integer)
    goods_value = Column(Float)
    weight_actual = Column(Float)
    weight_cft = Column(Float)
    weight_charge = Column(Float)
    rate = Column(Float)
    freight = Column(Float)

    pickup_cartage = Column(Float)
    misc_cartage = Column(Float)
    drop_cartage = Column(Float)
    hamali = Column(Float)
    op_hamali = Column(Float)
    valuation = Column(Float)
    doc_fee = Column(Float)
    gst_percent = Column(Float)
    
    payment_type = Column(String)
    method_of_payment = Column(String)
    account_number = Column(String, nullable=True)
    reference_id = Column(String, nullable=True)

    created_at = Column(DateTime)
