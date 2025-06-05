# 🧘 Fitness Studio Booking API

A simple FastAPI backend for managing fitness class bookings (Yoga, Zumba, HIIT). Designed for beginners and small projects using in-memory storage.

---

## 🚀 Features

- View available fitness classes
- Book a spot in a class
- Fetch bookings by email
- Easy-to-read code, great for learning FastAPI

---

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Language**: Python 3.9+
- **In-memory storage** (No external DB required)

---

## 📦 Installation

1. **Clone this repo**

```bash
git clone https://github.com/your-username/fitness-booking-api.git
cd fitness-booking-api
run  uvicorn main:app --reload
```



## Api Endpoints 

1. GET http://127.0.0.1:8000/classes => TO GET THE LIST OF CLASSES
2. POST http://127.0.0.1:8000/book  => TO BOOK THE CLASS
3. http://127.0.0.1:8000/bookings?email=EMAIL => TO GET THE LIST OF BOOKED CLASSES
