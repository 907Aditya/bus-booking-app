from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
import os
from database import get_db

from routers import users, buses, bookings, cargo  # ✅ Add cargo
import models
from database import engine
from sqlalchemy.orm import Session
from fastapi import Depends
# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# Static and templates folder
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(buses.router, prefix="/buses", tags=["Buses"])
app.include_router(bookings.router, prefix="/bookings", tags=["Bookings"])
app.include_router(cargo.router, prefix="/cargo", tags=["Cargo"])  # ✅ Add this
app.include_router(cargo.router, prefix="/cargo", tags=["Cargo"])  # ✅ Add cargo routes



@app.get("/cargo/view/{cargo_id}", response_class=HTMLResponse)
def view_cargo_receipt(cargo_id: int, request: Request, db: Session = Depends(get_db)):
    cargo = db.query(models.Cargo).filter(models.Cargo.id == cargo_id).first()
    if not cargo:
        return HTMLResponse(content="<h2>Cargo Not Found</h2>", status_code=404)
    return templates.TemplateResponse("cargo_receipt.html", {"request": request, "cargo": cargo})

