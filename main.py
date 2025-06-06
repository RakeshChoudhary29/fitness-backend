# main.py
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from uuid import uuid4
from datetime import datetime
import pytz
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

IST = pytz.timezone("Asia/Kolkata")

# In-memory DB
classes = []
bookings = []

# Models
class FitnessClass(BaseModel):
    id: str
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

class BookingRequest(BaseModel):
    class_id: str
    client_name: str
    client_email: EmailStr

class Booking(BaseModel):
    id: str
    class_id: str
    client_name: str
    client_email: EmailStr
    class_name: str
    datetime: datetime

# Seed Data
def seed_data():
    global classes
    now = datetime.now(IST)
    classes = [
        FitnessClass(id=str(uuid4()), name="Yoga", datetime=now.replace(hour=7, minute=0), instructor="Ramesh", available_slots=5),
        FitnessClass(id=str(uuid4()), name="Zumba", datetime=now.replace(hour=9, minute=0), instructor="Suresh", available_slots=3),
        FitnessClass(id=str(uuid4()), name="HIIT", datetime=now.replace(hour=18, minute=0), instructor="Rakesh", available_slots=2),
    ]

seed_data()


# change the timezone for the classes 

def change_timeZone(timezone:str):
    for cls in classes:
        cls.datetime=cls.datetime.astimezone(timezone)




#  endpoint to get all the classes 
@app.get("/classes", response_model=List[FitnessClass])
def get_classes():
    return classes

    

# endpoint to book a class     

@app.post("/book")
def book_class(booking_req: BookingRequest):
    print("here")
    for cls in classes:
        if cls.id == booking_req.class_id:
            if cls.available_slots <= 0:
                raise HTTPException(status_code=400, detail="No slots available")

            cls.available_slots -= 1
            booking = Booking(
                id=str(uuid4()),
                class_id=cls.id,
                client_name=booking_req.client_name,
                client_email=booking_req.client_email,
                class_name=cls.name,
                datetime=cls.datetime
            )
            bookings.append(booking)
            logging.info(f"Booking confirmed for {booking_req.client_email} in class {cls.name}")
            return {"message": "Booking successful", "booking_id": booking.id}
    raise HTTPException(status_code=404, detail="Class not found")



#  endpoint to check for the bookings     

@app.get("/bookings", response_model=List[Booking])
def get_bookings(email: EmailStr):
    result = [b for b in bookings if b.client_email == email]
    if not result:
        raise HTTPException(status_code=404, detail="No bookings found for this email")
    return result

# Run using: uvicorn main:app --reload
